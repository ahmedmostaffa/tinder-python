from seleniumwire import webdriver  # Import seleniumwire
from time import sleep
from Actions import Actions

options = webdriver.ChromeOptions()
options.add_argument("--allow-geolocation") 
options.add_argument('--disable-infobars')
options.add_argument('--disable-notifications')
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome()

driver.get('https://tinder.com/app/matches')
driver.implicitly_wait(30)
action=Actions(driver);
number_of_swipes=20

for i in number_of_swipes:
    try:
        action.like()
        driver.wait_for_request('recs/core?locale=en')
        for request in driver.requests:
            if request.url == 'https://api.gotinder.com/v2/recs/core?locale=en':
                print("reuqets have been found with " + request.url)
                print(request.response.body)
            del driver.requests       
    except:
        action.handleMybeLater()

# Access requests list via the `requests` attribute
    
        