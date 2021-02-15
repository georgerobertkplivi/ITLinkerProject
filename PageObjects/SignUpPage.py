from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
from Configs.CommonData import CommonData

class SignUpPage:

    #SignUpPage Locators
    img_logo_xpath = "//a/img[1]"
    lnk_signup_xpath = "//a[@class='signup-l']"
    btn_signup_xpath = "//li[@id='rslides1_s2']/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[@class='button' and 1]"
    btn_login_xpath = "//a[@id='loginButton']/span[1]"
    signup_page_title = "OnTrade - World financial affiliate program"

    # Signup Page Form Locators
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "reg_email"
    txt_password_name = "reg_pass"
    txt_confirm_password_name = "retry_reg_pass"
    btn_on_signup_page_xpath = "//input[@class='input_submit']"
    lnk_logout_linktext = "Logout"

    #Driver Path
    driver_path = CommonData.getDriverPath()


    def __init__(self,driver):
        self.driver = driver

    def setFirstName(self,firstname):
        browser = self.driver
        browser.find_element(By.NAME,self.txt_firstname_name).clear()
        browser.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)

    def setLastName(self,lastname):
        browser = self.driver
        browser.find_element(By.NAME, self.txt_lastname_name).clear()
        browser.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)

    def setEmail(self,email):
        browser = self.driver
        browser.find_element(By.NAME, self.txt_email_name).clear()
        browser.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self,password):
        browser = self.driver
        browser.find_element(By.NAME, self.txt_password_name).clear()
        browser.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def setConfimPassword(self,confirm_password):
        browser = self.driver
        browser.find_element(By.NAME, self.txt_confirm_password_name).clear()
        browser.find_element(By.NAME, self.txt_confirm_password_name).send_keys(confirm_password)

    def clickButtonOnSignUpPage(self):
        browser = self.driver
        browser.find_element(By.XPATH, self.btn_on_signup_page_xpath).click()

    def clickSignUpButtonOnHomePage(self):
        browser = self.driver
        browser.find_element(By.XPATH, self.btn_signup_xpath).click()

    def clickLogoutButton(self):
        browser = self.driver
        browser.find_element(By.LINK_TEXT, self.lnk_logout_linktext).click()

    def clickLogintButton(self):
        browser = self.driver
        browser.find_element(By.XPATH, self.btn_login_xpath).click()

    def closeBrowser(self):
        browser = self.driver
        browser.close()





