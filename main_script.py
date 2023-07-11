from seleniumwire import webdriver  # Import seleniumwire
import time
from Actions import Actions

driver = webdriver.Chrome()
 
driver.get('https://tinder.com/app/recs')
time.sleep(100)
driver.implicitly_wait(30)

action=Actions(driver);
action.like()
 
# Access requests list via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            
            request.response.status_code,
            request.response.headers['Content-Type']
        )

        