
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\odiin\Documents\chrome driver\chromedriver.exe")
browser.implicitly_wait(7)

url = 'https://www.instagram.com/?hl=en'
browser.get( url )

login_link = browser.find_element_by_xpath("//a[text()='log in']")
login_link.click()

sleep(3)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(" ")
username_input.send_keys(" ")

login_button = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")
login_button.click()

sleep(5)

browser.close()
