from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('driver', help='the absolute location to the Chrome driver')
parser.add_argument('email', help='the email address you use to login to bcs')
parser.add_argument('password', help='login password')

args = parser.parse_args()


def login(b):
    b.find_element_by_id('emailAddress').send_keys(args.email)
    b.find_element_by_id('password').send_keys(args.password)
    b.find_element_by_class_name('btn-submit').send_keys(Keys.ENTER)


def gradebook(b):
    # todo can we get rid of that sleep?
    time.sleep(1)
    # improve this to do some sort of search
    b.find_element(By.XPATH, '//tbody/tr[1]').click()
    b.find_element(By.XPATH, '//tbody/tr[2]').click()
    b.find_element_by_class_name('fa-graduation-cap').click()


if __name__ == '__main__':
    browser = webdriver.Chrome(args.driver)
    browser.get('https://bootcampspot-v2.com/login')
    login(browser)
    gradebook(browser)
