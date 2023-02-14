from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

email = "anna_nikolenko_06_123@yandex.ru"
password = "123456"


class TestEnter:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_come_in_by_enter_button(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # вход через кнопку Личный кабинет
    def test_come_in_by_account_button(self, driver):
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # вход через кнопку в форме регистрации
    def test_come_in_by_registration_form(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # вход через кнопку в форме восстановления пароля
    def test_come_in_by_recovery_password_button(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # переход в личный кабинет
    def test_come_in_to_account(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]"))
        )
        assert driver.find_element(By.XPATH, "//a[contains(text(),'Профиль')]")

    # переход из личного кабинета в конструктор
    def test_come_to_constructor_from_account(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]"))
        )
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        assert driver.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]")

    # выход из аккаунта
    def test_exit_from_account(self, driver):
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input [@name='name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]"))
        )
        driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти')]"))
        )





