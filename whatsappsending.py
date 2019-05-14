import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chromedriver = ('/Users/duhhhhhh/Documents/whatsapp/chromedriver')
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)


# add numbers with country code without any prefixes eg. +
numbers = [
919082396014
]

for i in numbers:
	# whatsapp API to be called
	driver.get("https://api.whatsapp.com/send?phone=" + str(i))

	# redirect to the web.whatsapp by clicking message btn
	redirect_btn = driver.find_element_by_id("action-button")
	redirect_btn.click()

	# wait for enough time (in secs) for whatsapp to find the element either by xpath or driver
	wait = WebDriverWait(driver, 50)

	# type in the message to be send
	message = "Hi there!" 

	# try block: to execute valid numbers and except: to intercept invalid numbers (have to wait for above seconds in order to catch the exception)
	try:
		inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
		input_box = wait.until(EC.visibility_of_element_located((By.XPATH, inp_xpath)))
		input_box.send_keys(message + Keys.ENTER)
		print (str(i) + ' - msg sent')
	except:
		err_btn = driver.find_element_by_class_name("_1WZqU")
		err_btn.click()
		print (str(i) + ' - invalid number')

	# pause the program for x seconds to fool whatsapp :P
	time.sleep(6)