from selenium import webdriver
from selenium.webdriver.common.by import By

class Locators:
    #Страница регистрации
    SIGN_UP_LINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    INPUT_NAME = (By.XPATH, "//fieldset[1]/div/div/child::input[@name='name']")
    INPUT_EMAIL = (By.XPATH, "//fieldset[2]/div/div/child::input[@name='name']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    SIGN_UP_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ссылка на вход возле "Уже зарегистрированы?"
    ENTER_LINK = (By.XPATH, "//a[@href='/login']")
    # Сообщение о неверном пароле
    WRONG_PASSWORD_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    #Страница авторизации
    ENTER_TEXT = (By.XPATH, "//h2[text() = 'Вход']")
    INPUT_EMAIL_AUTH = (By.XPATH, ".//fieldset[1]/div/div/input")
    INPUT_PASSWORD_AUTH = (By.XPATH, ".//fieldset[2]/div/div/input")
    ENTER_BUTTON = (By.XPATH, ".//button[text()= 'Войти']")
    ENTER_LINK = (By.XPATH, "//a[@href = '/login']")
    FORGET_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

    #Кнопка "Личный кабинет" на главной
    PROFILE_BUTTON = (By.XPATH, "//a[@href = '/account']")
    #Ссылка "Профиль" в личном кабинете
    PROFILE_LINK = (By.XPATH, "//a[@href = '/account/profile']")
    ENTER_LINK_IN_PROFILE = (By.XPATH, "//button[text() = 'Выход']")

    #Главная страница
    SIGN_IN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")

    #Страница восстановления пароля
    ENTER_LINK_FORGET_PASSWORD = (By.LINK_TEXT, "Войти")
    #Ссылка на конструктор в личном кабинете
    CONSTRUCTOR_LINK = (By.XPATH, ".//nav/ul/li/a[@href = '/']")

    SAUCES_LINK = (By.XPATH, "//span[text() = 'Соусы']")
    BUNS_LINK = (By.XPATH, "//span[text() = 'Булки']")
    FILLINGS_LINK = (By.XPATH, "//span[text() = 'Начинки']")
    BUN_HEADER = (By.XPATH, "//h2[text() = 'Булки']")
    SAUCES_HEADER =  (By.XPATH, "//h2[text() = 'Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text() = 'Начинки']")
    STELLAR_BURGERS_LOGO = (By.XPATH, "//nav/div/a")

