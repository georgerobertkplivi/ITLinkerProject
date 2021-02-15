import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from PageObjects.SignUpPage import SignUpPage
from Configs.CommonData import CommonData

class TestSignUp:
    baseURL = CommonData.getUrl()
    email = CommonData.getEmail()
    password = CommonData.getPassword()
    firstname = "George"
    lastname = "Robert"

    def test_signup_register_001(self):
        global  wait
        # self.exepath = CommonData.getDriverPath
        self.driver = webdriver.Chrome(executable_path="C:/Users/mm195/PycharmProjects/pythonProject/drivers/chromedriver.exe")
        self.driver.get(self.baseURL)
        wait = WebDriverWait(self.driver, 10)

        # Initiating the SignUp Class
        self.signup = SignUpPage(self.driver)
        self.signup.setFirstName(self.firstname)
        self.signup.setLastName(self.lastname)
        self.signup.setEmail(self.email)
        self.signup.setPassword(self.password)
        self.signup.setConfimPassword(self.password)
        self.signup.clickButtonOnSignUpPage()




