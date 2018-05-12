from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('driver', help='the absolute location to the Chrome driver')
parser.add_argument('email', help='the email address you use to login to bcs')
parser.add_argument('password', help='the password for said email address')

args = parser.parse_args()


def login():
    browser.find_element_by_id('emailAddress').send_keys(args.email)
    browser.find_element_by_id('password').send_keys(args.password)
    browser.find_element_by_class_name('btn-submit').send_keys(Keys.ENTER)

if(__name__ == '__main__'):
    browser = webdriver.Chrome(args.driver)
    browser.get('https://bootcampspot-v2.com/login')
    login()
