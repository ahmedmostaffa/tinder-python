from seleniumwire import webdriver  # Import seleniumwire
from time import sleep
from Actions import Actions


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--allow-geolocation')

sw_options = {
    'proxy': {
        'https': 'https://localhost:9222'
    }
}
driver = webdriver.Chrome(
    options=chrome_options,
    seleniumwire_options=sw_options,
)



driver.get('https://tinder.com/')
driver.implicitly_wait(30)
action=Actions(driver);

# main creteria here is caching core endpoint 
# sleep actions random 
# slee



for i in range(20):
    try:
        action.like_dislike()
        # 
        driver.wait_for_request('recs/core?locale=en')
        for request in driver.requests:
            if request.url == 'https://api.gotinder.com/v2/recs/core?locale=en':
                print("reuqets have been found with " + request.url)
                print(request.response.body)
            del driver.requests       
    except:
        action.handleMybeLater()


# Access requests list via the `requests` attribute
    
        