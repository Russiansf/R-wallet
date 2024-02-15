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

load_dotenv()

useragent = UserAgent()

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--window-size=1360,768')
options.add_argument(f'user-agent={useragent.random}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-features=ImprovedCookieControls')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.page_load_strategy = 'normal' # eager normal

options.add_extension(os.getcwd()+f'/ACMACODKJBDGMOLEEBOLMDJONILKDBCH_0_92_38_0.crx')
# options.add_argument('--enable-extensions')

privat_keys = [os.environ[f"u{i}"] for i in range(1, 14)]

rabbi_extension = 'chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/popup.html#/no-address'

private_key_button = ('xpath','//div[text()="Import Private Key"]')
input_password = ('xpath','//input[@id="password"]')
confirm_password = ('xpath','//input[@id="confirmPassword"]')
submit_button = ('xpath','//button[@type="submit"]')
enter_privat_key = ('xpath','//input[@placeholder="Enter your Private key"]')
button_confirm = ('xpath','//button')
more_btn_9 = ('xpath','(//div[@class="direction pointer"])[9]')
gastoken_btn = ('xpath','(//div[@class="field-slot"])[2]')
request_btn = ('xpath','//button[@type="button"]')
pop_up = ('xpath','(//div)[65]')
Uve_req_2day = ('xpath','//div[text()="You have requested today"]')


def run(privat_key, index):
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
    
    wait = WebDriverWait(driver, 10)

    try:
        # change_proxy()

        print(f'---------------Akk {index} start---------------')             	

        driver.get(url=rabbi_extension)

        # time.sleep(3)

        # driver.refresh()

        # time.sleep(3)
        try:
            step_1 = wait.until(ec.visibility_of_element_located((private_key_button)))
            step_1.click()
        except:
            driver.refresh()
            step_1.click()
        # driver.find_element(*private_key_button).click()

        # time.sleep(2) 
        wait.until(ec.visibility_of_element_located((input_password))).send_keys('12password!')                  
        # driver.find_element(*input_password).send_keys('12password!')    
        # time.sleep(2)
        driver.find_element(*confirm_password).send_keys('12password!')
        time.sleep(2)
        driver.find_element(*submit_button).click()
        time.sleep(2)
        driver.find_element(*enter_privat_key).send_keys(privat_key)
        driver.find_element(*button_confirm).click()
        time.sleep(1)

        driver.find_element(*button_confirm).click()
                
        time.sleep(1)

        driver.find_element(*pop_up).send_keys(Keys.ESCAPE)

        driver.find_element(*more_btn_9).click()
        time.sleep(1)
        driver.find_element(*gastoken_btn).click()
        time.sleep(1)
        # driver.find_element(*request_btn).click()

        try:
            wait.until(ec.visibility_of_element_located((Uve_req_2day)))
            print(f'-----------Already requested-------------')
        except:
            wait.until(ec.visibility_of_element_located((request_btn))).click()
            print(f'------------------end--------------------')          

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
        n = (input('Введи ключ: '))
        for i, z_privat_key in enumerate(privat_keys):
            zkey = int(z_privat_key) + int(n)
            privat_key = hex(int(zkey))            
            if z_privat_key[0] == '0':      
                privat_key = privat_key[:2] + '0' + privat_key[2:]
            else:
                privat_key
                        
            run(privat_key,i+1)



if __name__ == '__main__':
    main()
