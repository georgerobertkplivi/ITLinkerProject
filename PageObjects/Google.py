from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

#Google.py File
class Google:
    txtbox_searchbar_xpath = "//input[@class='gLFyf gsfi']"

    def __init__(self,driver):
        self.driver = driver

    def enterSearchTerm(self,search_term):
        browser = self.driver
        browser.find_element(By.XPATH, self.txtbox_searchbar_xpath).claer()
        # self.driver.find_element(By.XPATH, self.txtbox_searchbar_xpath).send_keys(search_term,Keys.RETURN)