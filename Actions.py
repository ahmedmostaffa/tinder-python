from seleniumwire import webdriver
from time import sleep
class Actions:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def like(self):
        like_button = self.driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        self.click(like_button);

    def nope(self):
        nope_button = self.driver.find_element(by='xpath', value='//button//span[text()="Nope"]')
        self.click(nope_button);
    


    
    def login(self, username,password):
        
        login_btn=self.driver.find_element(by='xpath',value='//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login_btn.click()

        # switch to login popup
        base_window = self.driver.switch_to.window('')
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()


    def click(self,elem):
        self.driver.execute_script("arguments[0].click();",elem) 
          