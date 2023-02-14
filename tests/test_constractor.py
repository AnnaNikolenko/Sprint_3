from selenium.webdriver.common.by import By


class TestConstractor:
    def test_switch_to_section_bulki(self, driver):
        active_tab = driver.find_element(By.XPATH, ("//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")).text
        assert active_tab == "Булки"

    def test_switch_to_section_souses(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        active_tab = driver.find_element(By.XPATH, (
            "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")).text
        assert active_tab == "Соусы"

    def test_switch_to_section_fillings(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        active_tab = driver.find_element(By.XPATH, (
            "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")).text
        assert active_tab == "Начинки"


