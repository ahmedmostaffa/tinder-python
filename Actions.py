from seleniumwire import webdriver
from time import sleep
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
        
    


    
    def login(self, phoneNumber:str):
        self.driver.find_element(by='xpath',value='//div[text()="Log in"]').click()
        # self.driver.find_element(by='xpath',value='//div[contains(text(),"Facebook")]').click()
        # self.driver.find_element(by='css_selector',value='input[name="phone_number"]').click()
        
        '''
        # switch to login popup
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        self.driver.find_element(by='xpath',value='//input[@name="login"]').click()

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()
        '''
    def wait(self):
        while((self.driver.current_url!='https://tinder.com/app/recs')):
            sleep(5)
        

    def click(self,elem):
        self.driver.execute_script("arguments[0].click();",elem) 
          