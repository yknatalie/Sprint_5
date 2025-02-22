from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSignOut:
    def test_sign_out_from_profile(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        driver.find_element(*Locators.INPUT_EMAIL_AUTH).send_keys(Data.REGISTER_AUTH_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD_AUTH).send_keys(Data.REGISTER_AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.PROFILE_LINK,
                                                                        "Профиль"))
        driver.find_element(*Locators.ENTER_LINK_IN_PROFILE).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        enter = driver.find_element(*Locators.ENTER_TEXT)
        assert enter.is_displayed()