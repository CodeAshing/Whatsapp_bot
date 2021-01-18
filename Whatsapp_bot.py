
from selenium import webdriver
import os
def main():
	driver = webdriver.Firefox(executable_path="./geckodriver")
	driver.get('https://web.whatsapp.com/')

	name = input('Enter the name of user or group: ')
	msg = input('Enter your message: ')
	count = int(input('Enter the count: '))

	input('Enter any key after scanning QR code')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	msg_box = driver.find_element_by_xpath('//div[@data-tab = "6"]')
		
	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_2Ujuu')
		button.click() 
	print('Complete!!')

main()