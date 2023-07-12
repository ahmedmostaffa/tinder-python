from seleniumwire import webdriver  # Import seleniumwire
from time import sleep
from Actions import Actions

options = webdriver.ChromeOptions()
options.add_argument("--allow-geolocation") 
options.add_argument('--disable-infobars')
options.add_argument('--disable-notifications')

driver = webdriver.Chrome()

driver.get('https://tinder.com/app/matches')
# time.sleep(100)
driver.implicitly_wait(30)

action=Actions(driver);
action.login("d")

action.like()
action.nope()
 
# Access requests list via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            request.response.status_code,
            request.response.headers['Content-Type']
        )

        