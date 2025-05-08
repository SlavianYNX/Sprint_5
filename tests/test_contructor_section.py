from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import Person
from tests.locators import AccountLogin, PersonalAccount
from tests.urls import *


class TestConstruction:

    def test_section_bun(self, driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.pers_account))
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_construct))
        driver.find_element(*PersonalAccount.button_construct).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_bun))
        bun_butt = driver.find_element(*PersonalAccount.button_bun).text
        assert bun_butt == 'Булки'


    def test_section_sauce(self, driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.pers_account))
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_construct))
        driver.find_element(*PersonalAccount.button_construct).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_sauce))
        sauce_butt = driver.find_element(*PersonalAccount.button_sauce).text
        assert sauce_butt == 'Соусы'


    def test_section_filling(self,driver):
        driver.get(PageUrls.main_page)
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(AccountLogin.button_enter))
        driver.find_element(*AccountLogin.email_auth).send_keys(Person.email)
        driver.find_element(*AccountLogin.pass_auth).send_keys(Person.password)
        driver.find_element(*AccountLogin.button_enter).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.pers_account))
        driver.find_element(*PersonalAccount.pers_account).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_construct))
        driver.find_element(*PersonalAccount.button_construct).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccount.button_filling))
        filling_butt = driver.find_element(*PersonalAccount.button_filling).text
        assert filling_butt == 'Начинки'
