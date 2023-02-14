import pytest
import re
from faker import Faker
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

faker = Faker()
email = faker.email()
name = "Anna"
password = "123456"


class TestRegistration:
    # проверка успешной регистрации
    def test_registration_successful(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "(//input [@name='name']) [1]").send_keys(name)
        driver.find_element(By.XPATH, "(//input [@name='name']) [2]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")

    # при незаполненном поле Имя регистрации не происходит
    def test_registration_with_empty_name(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "(//input [@name='name']) [1]").send_keys("")
        driver.find_element(By.XPATH, "(//input [@name='name']) [2]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        with pytest.raises(TimeoutException):
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        with pytest.raises(NoSuchElementException):
            assert not driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")

    # проверка, что введен валидный емейл
    def test_valid_email(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "(//input [@name='name']) [1]").send_keys("")
        driver.find_element(By.XPATH, "(//input [@name='name']) [2]").send_keys(email)
        assert bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email))

    # при вводе емейла без @ регистрации не происходит
    def test_invalid_email(self, driver):
        email = "wjehdwwfwigrf1223.com"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "(//input [@name='name']) [1]").send_keys("")
        driver.find_element(By.XPATH, "(//input [@name='name']) [2]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        with pytest.raises(TimeoutException):
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))
        with pytest.raises(NoSuchElementException):
            assert not driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")

    # при вводе паспорта короче 6 символов, появляется сообщение об ошибке
    def test_passwort_less_6_symbols(self, driver):
        password = "1221"
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "(//input [@name='name']) [1]").send_keys("")
        driver.find_element(By.XPATH, "(//input [@name='name']) [2]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

