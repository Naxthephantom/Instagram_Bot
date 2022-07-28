
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome( r'C:\Users\odiin\Documents\chrome driver\chromedriver.exe')
browser.implicitly_wait(7)

url = 'https://www.instagram.com/?hl=en'
browser.get( url )

sleep(10)

login_link = browser.find_element_by_xpath("//a[text()='log in']")
login_link.click()

sleep(7)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(" <your username> ")
password_input.send_keys(" <your username> ")

login_button = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")
login_button.click()

sleep(5)

browser.close()

#Now this is the way one would normally open the instagram app on their browser and login into their instagram account.
#This is a detailed code breaking down the process step by step.
#But there is a method that is easier, shorter and faster.
#By using instapy, all this can been shortend to a line of code.
#Check the other python file for more information on using instapy.
