from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/chromedriver.exe')
#Starts our driver and goes to the starting webpage which is google.com
driver = webdriver.Chrome(service=s)

driver.get('https://google.com')

#Inputs text into the google search box
input_box = driver.find_element("xpath", 'html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys('google')

#Presses the enter button to search
input_box.send_keys(Keys.ENTER)
time.sleep(2)
