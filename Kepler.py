import os
from selenium import webdriver
import time
from dotenv import load_dotenv
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import pickle
from change_proxy import change_proxy
# для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

# load_dotenv()

useragent = UserAgent()

PROXY_SERVER = 'rYmZyQ:daeaS7ys4Eh8@wproxy.site:11842'

options = webdriver.ChromeOptions()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument("–disable-gpu")
# options.add_argument("--headless=new")
# options.add_argument('--window-size=400,768')
options.add_argument(f'user-agent={useragent.random}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-features=ImprovedCookieControls')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.page_load_strategy = 'normal' # eager normal
# options.add_argument(f'--proxy-server={PROXY_SERVER}')
options.add_extension(os.getcwd()+f'/Keplr(0.12.52)2023-12-18 .crx')
# options.add_argument('--enable-extensions')
# start_account = 1
# end_account = 14
# privat_keys = [os.environ[f"u{i}"] for i in range(start_account, end_account+1)]

plugin_file = 'proxy_auth_plugin.zip'
options.add_extension(plugin_file)


seed = 'risk gadget mass unfold distance fringe knee despair economy connect sniff between'


kepler_extension = 'chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/popup.html#'

# https://app.osmosis.zone/
# https://wallet.keplr.app/
# https://sifchain.akash.pro/
# https://chihuahua.omniflix.co/

xpath_import_wallet = '(//div[text()="Import an existing wallet"])[1]'
xpath_use_seed = '(//button)[4]'
xpath_input_seed = '(//input[@type="password"])[1]'
xpath_advanced = '(//button)[9]'
xpath_import = '(//button)[10]'
xpath_name = '//input[@name="name"]'
xpath_password = '//input[@name="password"]'
xpath_conf_password = '//input[@name="confirmPassword"]'
xpath_next = '(//button)[11]'
xpath_all_chains = '//div[@class="sc-fXynhf cnzXHR"]'
xpath_save = '//button'
xpath_terra = '//div[@class="sc-duzrYq fZdpMt"]'
xpath_import_terra = '//button'
xpath_finish = '//button'

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
'source': '''
	delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
	delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
	delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
	delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
	delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
	delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
'''
})

driver.get(url=kepler_extension)
wait = WebDriverWait(driver, 10)
time.sleep(5)
# wait.until(ec.visibility_of_element_located((xpath_import_wallet))).click()
# wait.until(ec.visibility_of_element_located((xpath_use_seed))).click()
# wait.until(ec.visibility_of_element_located((xpath_input_seed))).send_keys(seed)
# wait.until(ec.visibility_of_element_located((xpath_advanced))).click()
# wait.until(ec.visibility_of_element_located((xpath_import))).click()
# wait.until(ec.visibility_of_element_located((xpath_name))).send_keys(seed)
# wait.until(ec.visibility_of_element_located((xpath_password))).send_keys('zxcqwe5288352')
# wait.until(ec.visibility_of_element_located((xpath_conf_password))).send_keys('zxcqwe5288352')
# wait.until(ec.visibility_of_element_located((xpath_next))).click()
# wait.until(ec.visibility_of_element_located((xpath_save))).click()
# wait.until(ec.visibility_of_element_located((xpath_terra))).click()
# wait.until(ec.visibility_of_element_located((xpath_import_terra))).click()
# wait.until(ec.visibility_of_element_located((xpath_finish))).click()

input('Finish')

driver.close()
driver.quit()


# risk gadget mass unfold distance fringe knee despair economy connect sniff between
# rYmZyQ:daeaS7ys4Eh8