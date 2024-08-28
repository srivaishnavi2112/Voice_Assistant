from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Infow:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")
        search=self.driver.find_element(By.XPATH,'//*[@id="searchInput"]')
        search.send_keys(query)
        search.send_keys(Keys.RETURN) 
        input()
