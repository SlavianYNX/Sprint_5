from selenium.webdriver.common.by import By


class RegistrationLocators:
    name_field = (By.XPATH, ".//fieldset[1]/div/div/input[@name='name']") # Поле Имя
    email_field = (By.XPATH, ".//fieldset[2]/div/div/input[@name='name']") # Поле Email
    password_field = (By.XPATH, ".//form/fieldset[3]/div/div/input[@name='Пароль']")  # Поле Пароль
    button_registr = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться
    error_pass = (By.XPATH, ".//fieldset[3]/div/p[text()='Некорректный пароль']") # Сообщение об ошибке

class AccountLogin:
    button_login = (By.XPATH, ".//section[2]/div/button[text()='Войти в аккаунт']") # Кнопка Войти в Аккаунт
    email_auth = (By.XPATH, ".//fieldset[1]/div/div/input[@name='name']") # Поле Email в форме авторизации
    pass_auth = (By.XPATH, ".//fieldset[2]/div/div/input[@name='Пароль']") # Поле Пароль в форме авторизации
    button_enter = (By.XPATH, ".//div/form/button[text()='Войти']") # Кнопка Войти в форме авторизации
    button_enter_reg = (By.XPATH, ".//div/p/a[text()='Войти']") # Кнопка войти в форме регистрации
    button_enter_forgot = (By.XPATH, ".//div/p/a[text()='Войти']") # Кнопка Войти в форме восстановить пароль

class PersonalAccount:
    pers_account = (By.XPATH, ".//div[1]/div/header/nav/a/p[text()='Личный Кабинет']") # Кнопка Личный кабинет на главной странице
    button_exit = (By.XPATH, ".//div/nav/ul/li[3]/button[text()='Выход']") # Кнопка выход в личном кабинете
    button_construct = (By.XPATH, ".//div[1]/div/header/nav/ul/li[1]/a") # Кнопка конструктор в личном кабинете
    button_logo = (By.XPATH, ".//div/header/nav/div") # Логотип stella burger в личном кабинете
    button_sauce = (By.XPATH, ".//section[1]/div[1]/div[2]/span[text()='Соусы']") # Кнопка Соусы в Личном кабинете
    button_filling = (By.XPATH, "//section[1]/div[1]/div[3]/span[text()='Начинки']") # Кнопка Начинки в Личном кабинете
    button_bun = (By.XPATH, ".//section[1]/div[1]/div[1]/span[text()='Булки']") # Кнопка Булки в Личном кабинете
    place_order = (By.XPATH, ".//section[2]/div/button[text()='Оформить заказ']") # Кнопка Оформить заказ
    exit_button = (By.XPATH, ".//div/nav/ul/li[3]/button[text()='Выход']")
    save_button = (By.XPATH, ".//div/main/div/div/div/div/button[2][text()= 'Сохранить']")