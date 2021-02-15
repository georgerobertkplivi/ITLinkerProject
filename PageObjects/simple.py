# importing webdriver from selenium
from selenium import webdriver

# Here Chrome will be used
driver = webdriver.Chrome(executable_path="C:\\Users\\mm195\\PycharmProjects\\pythonProject\\drivers\\chromedriver.exe")


# URL of website
url = "https://www.python.org/"

# Opening the website
driver.get(url)

# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
print(get_title)
