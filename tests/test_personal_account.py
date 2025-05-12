from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Person
from locators import AccountLogin, PersonalAccount
from urls import *


class TestPersonalAccount:

    def test_transfer_account_main_page(self, driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.exit_button))
        save_b = driver.find_element(*PersonalAccount.exit_button).is_displayed()
        assert driver.current_url == PageUrls.profile_page and save_b


    def test_transfer_constructor(self, driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.exit_button))
        driver.find_element(*PersonalAccount.button_construct).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_construct))
        bun_butt = driver.find_element(*PersonalAccount.button_construct).is_displayed()
        assert driver.current_url == PageUrls.main_page and bun_butt


    def test_transfer_logo_stella(self, driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_logo))
        driver.find_element(*PersonalAccount.button_logo).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.place_order))
        bun_but = driver.find_element(*PersonalAccount.place_order).is_displayed()
        assert driver.current_url == PageUrls.main_page and bun_but


    def test_logout_account(self, driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.exit_button))
        driver.find_element(*PersonalAccount.exit_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        exit_butt = driver.find_element(*AccountLogin.button_enter).is_displayed()
        assert  driver.current_url == PageUrls.auth_page and exit_butt