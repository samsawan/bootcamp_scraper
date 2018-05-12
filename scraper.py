from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--driver', help='the absolute location to the Chrome driver')
parser.add_argument('--email', help='the email address you use to login to bcs')
parser.add_argument('--password', help='the password for said email address')

args = parser.parse_args()
print(args)

# paramertize this
# browser = webdriver.Chrome(executable_path='/Users/ssawan/bin/chromedriver')
# browser.get('https://bootcampspot-v2.com/login')
#
# # paramertize this
# browser.find_element_by_id('emailAddress').send_keys('ssawan623@gmail.com')
# # paramertize this
# browser.find_element_by_id('password').send_keys('------')
