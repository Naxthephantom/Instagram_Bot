
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.binary_location = ( "C:\Users\Public\Desktop\Brave.lnk" )
driver_path = ( "C:\Users\odiin\Documents\chrome driver\chromedriver.exe" )
driver = webdriver.Chrome(options = Options, executable_path = driver_path)

browser = webdriver.chrome()
browser.implicitly_wait(7)

url = 'https:www.instagram.com/?hl=en'
browser.get( url )

login_link = browser.find_element_by_xpath("//a[text()='log in']")
login_link.click()

sleep(5)

browser.close()
