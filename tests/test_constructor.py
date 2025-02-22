from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor:
    def test_buns_scroll(self, driver):
        driver.find_element(*Locators.BUNS_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_HEADER))

        buns_header = driver.find_element(*Locators.BUN_HEADER)
        assert buns_header.is_displayed()

    def test_sauces_scroll(self, driver):
        driver.find_element(*Locators.SAUCES_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SAUCES_HEADER))

        sauces_header = driver.find_element(*Locators.SAUCES_HEADER)
        assert sauces_header.is_displayed()

    def test_fillings_scroll(self, driver):
        driver.find_element(*Locators.FILLINGS_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.FILLINGS_HEADER))

        fillings_header = driver.find_element(*Locators.FILLINGS_HEADER)
        assert fillings_header.is_displayed()

