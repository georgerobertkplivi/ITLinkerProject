from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Google import Google
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


#test_google.py
class TestGoogle001:

    url = "https://www.google.com/"
    search_word = "Python.org"
    searchbar_xpath ="//input[@class='gLFyf gsfi']"

    def test_setup(self):
        global driver
        global wait
        driver = webdriver.Chrome(executable_path="C:/Users/mm195/PycharmProjects/pythonProject/drivers/chromedriver.exe")
        wait = driver.implicitly_wait(10)


    def test_searchGoogle(self):
        driver.get(self.url)
        # Initiate Google Class
        google = Google(driver)
    #     wait.until(
    #     ec.presence_of_element_located((By.ID, self.searchbar_xpath))
    # )
    #     google.enterSearchTerm(self.search_word)
        act_title = driver.title
        if act_title == "Google":
            assert True
        else:
            assert False

