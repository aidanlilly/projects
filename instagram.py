#Aidan Lilly
#December 20, 2021
#Web scraping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

user = "" #Variables left unassigned for privacy reasons
password = ""
recipient = ""
txt = "Hello!"
numOfMsgs = 100


PATH = "C:\Program Files (x86)\chromedriver.exe" #Locate chromedriver application

driver = webdriver.Chrome(ChromeDriverManager().install()) #Run chrome
driver.implicitly_wait(5)

driver.get('https://www.instagram.com/') #Go to instagram website

driver.implicitly_wait(10)

user_input = driver.find_element_by_css_selector("input[name='username']") #Find textbox for username and password
pass_input = driver.find_element_by_css_selector("input[name='password']")

user_input.send_keys(user) #Input relevant information to textboxes
pass_input.send_keys(password)

pass_input.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

DM = driver.find_element_by_class_name("xWeGp") #Find direct message button
DM.click() #Click it

driver.implicitly_wait(10)

DeclNoti = driver.find_element_by_xpath('//button[text()="Not Now"]') #Clear pop up on screen
DeclNoti.click()

driver.implicitly_wait(10)

inbox = driver.find_element_by_xpath(f'//div[text()="{recipient}"]') #Find recipient in inbox
inbox.click()

driver.implicitly_wait(10)


message = driver.find_element_by_xpath('//textarea[@placeholder="Message..."]') #Find textbox for DM

for i in range(numOfMsgs): #Send messages
  message.send_keys(txt)
  message.send_keys(Keys.RETURN)