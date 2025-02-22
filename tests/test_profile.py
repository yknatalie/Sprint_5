from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProfile:
    def test_profile_button(self, driver):
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
        profile_link = driver.find_element(*Locators.PROFILE_LINK)

        assert profile_link.is_displayed()

    def test_constructor_from_profile(self, driver):
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
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.SAUCES_LINK, "Соусы"))
        sauces = driver.find_element(*Locators.SAUCES_LINK)

        assert sauces.is_displayed()

    def test_logo_from_profile(self, driver):
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
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element(Locators.SAUCES_LINK, "Соусы"))
        sauces = driver.find_element(*Locators.SAUCES_LINK)

        assert sauces.is_displayed()