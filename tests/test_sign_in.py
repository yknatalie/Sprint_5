from data import Data
from helper import Helper
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestSignIn:
    def test_sign_in_button_on_main_page(self,driver):
        driver.find_element(*Locators.SIGN_IN_BUTTON_MAIN_PAGE).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        driver.find_element(*Locators.INPUT_EMAIL_AUTH).send_keys(Data.REGISTER_AUTH_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD_AUTH).send_keys(Data.REGISTER_AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON))

        profile_button = driver.find_element(*Locators.PROFILE_BUTTON)

        assert profile_button.is_displayed()

    def test_sign_up_with_profile_button(self,driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        driver.find_element(*Locators.INPUT_EMAIL_AUTH).send_keys(Data.REGISTER_AUTH_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD_AUTH).send_keys(Data.REGISTER_AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON))

        profile_button = driver.find_element(*Locators.PROFILE_BUTTON)

        assert profile_button.is_displayed()

    def test_sign_in_in_sign_up_form(self,driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_LINK).click()
        driver.find_element(*Locators.ENTER_LINK).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        driver.find_element(*Locators.INPUT_EMAIL_AUTH).send_keys(Data.REGISTER_AUTH_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD_AUTH).send_keys(Data.REGISTER_AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON))

        profile_button = driver.find_element(*Locators.PROFILE_BUTTON)

        assert profile_button.is_displayed()

    def test_sign_in_in_password_recovery_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.FORGET_PASSWORD_LINK).click()
        driver.find_element(*Locators.ENTER_LINK_FORGET_PASSWORD).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        driver.find_element(*Locators.INPUT_EMAIL_AUTH).send_keys(Data.REGISTER_AUTH_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD_AUTH).send_keys(Data.REGISTER_AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON))

        profile_button = driver.find_element(*Locators.PROFILE_BUTTON)

        assert profile_button.is_displayed()






