from selenium import webdriver
import time

status = 'None'
change_proxy_ip = 'https://changeip.mobileproxy.space/?proxy_key=3101c73e350650f60e5225492f6ccb91'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

def change_proxy():
	driver = webdriver.Chrome(options=options)
	driver.get(url=change_proxy_ip)
	try:
		driver.find_element('xpath', '//div[text()="Смена прошла успешно"]')
		status = 'The proxy IP has changed :)'
	except:
		status = 'The proxy IP has not changed :('
	time.sleep(1)
	driver.close()
	driver.quit()
	print(status)
