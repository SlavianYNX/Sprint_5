from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Person, ConstructionModuleData
from locators import AccountLogin, PersonalAccount
from urls import *


class TestLogin:

    def test_log_in_account(self, driver):
        driver.get(PageUrls.main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_login))
        driver.find_element(*AccountLogin.button_login).click()
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.place_order))
        place_orders = driver.find_element(*PersonalAccount.place_order).text
        assert driver.current_url == PageUrls.main_page and place_orders == ConstructionModuleData.text_orders


    def test_login_personal_account(self, driver):
        driver.get(PageUrls.main_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.pers_account))
        driver.find_element(*PersonalAccount.pers_account).click()
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.place_order))
        place_orders = driver.find_element(*PersonalAccount.place_order).text
        assert place_orders == ConstructionModuleData.text_orders


    def test_login_enter_form_registration(self, driver):
        driver.get(PageUrls.reg_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter_reg))
        driver.find_element(*AccountLogin.button_enter_reg).click()
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.place_order))
        place_orders = driver.find_element(*PersonalAccount.place_order).text
        assert driver.current_url == PageUrls.main_page and place_orders == ConstructionModuleData.text_orders


    def test_login_enter_form_forgot(self, driver):
        driver.get(PageUrls.forgot_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter_forgot))
        driver.find_element(*AccountLogin.button_enter_forgot).click()
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.place_order))
        place_orders = driver.find_element(*PersonalAccount.place_order).text
        assert driver.current_url == PageUrls.main_page and place_orders == ConstructionModuleData.text_orders
