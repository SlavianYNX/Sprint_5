from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Person, ConstructionModuleData
from locators import AccountLogin, PersonalAccount
from urls import PageUrls

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
        text_bun_but = driver.find_element(*PersonalAccount.button_bun).text
        assert text_bun_but == ConstructionModuleData.Bun


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
        text_sauce_but = driver.find_element(*PersonalAccount.button_sauce).text
        assert text_sauce_but == ConstructionModuleData.Sauce


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
        text_filling_but = driver.find_element(*PersonalAccount.button_filling).text
        assert text_filling_but == ConstructionModuleData.Filling
