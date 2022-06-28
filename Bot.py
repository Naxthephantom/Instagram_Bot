
from time import sleep
from selenium import webdriver

browser = webdriver.chromedriver()
browser.implicitly_wait(7)

url = 'https:www.instagram.com/?hl=en'

browser.get( url )

login_link = browser.find_element_by_xpath("//a[text()='log in']")
login_link.click()

sleep(5)

browser.close()
