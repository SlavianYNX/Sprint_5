from selenium.webdriver.common.by import By


class RegistrationLocators:
    name_field = (By.XPATH, ".//input[@name='name']") # Поле Имя
    email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле Email
    password_field = (By.XPATH, "//input[@type='password']")  # Поле Пароль
    button_registr = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться
    error_pass = (By.XPATH, ".//p[text()='Некорректный пароль']") # Сообщение об ошибке

class AccountLogin:
    button_login = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка Войти в Аккаунт
    email_auth = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле Email в форме авторизации
    pass_auth = (By.XPATH, ".//input[@name='Пароль']") # Поле Пароль в форме авторизации
    button_enter = (By.XPATH, ".//button[text()='Войти']") # Кнопка Войти в форме авторизации
    button_enter_reg = (By.XPATH, ".//a[text()='Войти']") # Кнопка войти в форме регистрации
    button_enter_forgot = (By.XPATH, ".//p/a[text()='Войти']") # Кнопка Войти в форме восстановить пароль

class PersonalAccount:
    pers_account = (By.XPATH, ".//a/p[text()='Личный Кабинет']") # Кнопка Личный кабинет на главной странице
    button_exit = (By.XPATH, ".//button[text()='Выход']") # Кнопка выход в личном кабинете
    button_construct = (By.XPATH, ".//p[text()='Конструктор']") # Кнопка конструктор в личном кабинете
    button_logo = (By.XPATH, ".//div[@class ='AppHeader_header__logo__2D0X2']") # Логотип stella burger в личном кабинете
    button_sauce = (By.XPATH, ".//span[text()='Соусы']") # Кнопка Соусы в Личном кабинете
    button_filling = (By.XPATH, "//span[text()='Начинки']") # Кнопка Начинки в Личном кабинете
    button_bun = (By.XPATH, ".//span[text()='Булки']") # Кнопка Булки в Личном кабинете
    place_order = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка Оформить заказ
    exit_button = (By.XPATH, ".//button[text()='Выход']")
    save_button = (By.XPATH, ".//button[text()= 'Сохранить']")