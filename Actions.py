from seleniumwire import webdriver
class Actions:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def like(self):
        like_button = self.driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        self.click(like_button);


    def click(self,elem):
        self.driver.execute_script("arguments[0].click();",elem) 
          