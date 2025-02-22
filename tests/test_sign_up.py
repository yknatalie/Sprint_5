from data import Data
from helper import Helper
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSignUp:
    def test_sign_up_successful(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_LINK).click()

        name_input = driver.find_element(*Locators.INPUT_NAME)
        name_input.send_keys(Data.USER_NAME)

        email_input = driver.find_element(*Locators.INPUT_EMAIL)
        email = Helper.generate_email()
        email_input.send_keys(email)

        password_input = driver.find_element(*Locators.INPUT_PASSWORD)
        password = Helper.generate_password()
        password_input.send_keys(password)

        sign_up_button = driver.find_element(*Locators.SIGN_UP_BUTTON)
        sign_up_button.click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.ENTER_TEXT,
                                                                        "Вход"))
        auth_email = driver.find_element(*Locators.INPUT_EMAIL_AUTH)
        auth_email.send_keys(email)

        auth_password = driver.find_element(*Locators.INPUT_PASSWORD_AUTH)
        auth_password.send_keys(password)

        enter_button =driver.find_element(*Locators.ENTER_BUTTON)
        enter_button.click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PROFILE_LINK))
        profile_link = driver.find_element(*Locators.PROFILE_LINK)

        assert profile_link.is_displayed()

    def test_invalid_password(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_LINK).click()

        name_input = driver.find_element(*Locators.INPUT_NAME)
        name_input.send_keys(Data.USER_NAME)

        email_input = driver.find_element(*Locators.INPUT_EMAIL)
        email = Helper.generate_email()
        email_input.send_keys(email)

        password_input = driver.find_element(*Locators.INPUT_PASSWORD)
        password_input.send_keys(Data.INVALID_PASSWORD)

        sign_up_button = driver.find_element(*Locators.SIGN_UP_BUTTON)
        sign_up_button.click()

        invalid_password = driver.find_element(*Locators.WRONG_PASSWORD_MESSAGE)

        assert invalid_password.is_displayed()












