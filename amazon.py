from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import AMAZON_ID, AMAZON_PW

themore_url = "https://themorehelp.com/"
login_url = "https://www.amazon.com/-/ko/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
giftcard_url = "https://www.amazon.com/gp/product/B086KKT3RX"

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.0 Safari/537.36")
options.add_experimental_option("detach", True)
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
# options.add_argument('headless')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.delete_all_cookies()
driver.implicitly_wait(30)

# get the giftcard amount 
driver.get(themore_url)
giftcard_amount = driver.find_element_by_xpath('/html/body/div[1]/main/div[4]/div[4]/table/tbody/tr[1]/td[3]').text

# login 
driver.get(login_url)
driver.find_element_by_id('ap_email').send_keys(AMAZON_ID)
driver.find_element_by_id('continue').click()
driver.find_element_by_id('ap_password').send_keys(AMAZON_PW)
driver.find_element_by_id('signInSubmit').click()

# buy giftcard
sleep(3)
driver.get(giftcard_url)
driver.find_element_by_id('gcui-asv-reload-form-custom-amount').send_keys(giftcard_amount)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[4]/div[3]/div/div/div/div/div[1]/div/form/div[3]/span/span/input').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input').click()

# close
driver.close()
