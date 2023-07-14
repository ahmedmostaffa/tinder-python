from seleniumwire import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
class Actions:
    time=300
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def like(self):
        self.wait()
        like_button = self.driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        self.click(like_button);

    def nope(self):
        self.wait()
        nope_button = self.driver.find_element(by='xpath', value='//button//span[text()="Nope"]')
        self.click(nope_button);
    
    def printEndpoint(self):
        self.driver.wait_for_request('recs/core')

    def handleMybeLater(self):
        self.driver.find_element(by='xpath', value='//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]').click()

        

    
    def login(self, phoneNumber:str):
        self.driver.find_element(by='xpath',value='//div[text()="Log in"]').click()
    def wait(self):
        while(self.isPresent('//button//span[text()="Like"]')!=True):
            sleep(5)
        

    def click(self,elem):
        self.driver.execute_script("arguments[0].click();",elem) 
          
    def isPresent(self,xpath):
        try:
            self.driver.find_element(by='xpath',value=xpath)
        except NoSuchElementException:
                return False
        return True      