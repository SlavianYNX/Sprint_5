from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import RandomData, Person
from tests.locators import RegistrationLocators, AccountLogin, PersonalAccount
from tests.urls import *


class TestRegistration:

    def test_registration_form_stella(self, driver):
        driver.get(PageUrls.reg_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationLocators.button_registr))
        driver.find_element(*RegistrationLocators.name_field).send_keys(RandomData.name)
        driver.find_element(*RegistrationLocators.email_field).send_keys(RandomData.email)
        driver.find_element(*RegistrationLocators.password_field).send_keys(RandomData.password)
        driver.find_element(*RegistrationLocators.button_registr).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.place_order))
        butt__ = driver.find_element(*PersonalAccount.place_order).text
        assert driver.current_url == PageUrls.main_page and butt__


