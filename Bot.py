from time import sleep
from selenium import webdriver

browser = webdriver.brave()

url = 'https:www.instagram.com/?hl=en'

browser.get( url )

sleep(5)

browser.close()
