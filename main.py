import os
from selenium import webdriver
import time
from dotenv import load_dotenv
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains as AC

load_dotenv()

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument('--window-size=400,768')
options.add_argument(f'user-agent={useragent.random}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-features=ImprovedCookieControls')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.page_load_strategy = 'normal'

options.add_extension(os.getcwd()+f'/joohadbhjkdpjgdfnmkgndclmfbcdjen.crx')

start_account = 1
end_account = 15
privat_keys = [os.environ[f"u{i}"] for i in range(start_account, end_account+1)]

rabbi_extension = 'chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/popup.html#/no-address'
# rabbi_extension = 'chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/popup.html#/no-address'

private_key_button = ('xpath','//div[text()="Import Private Key"]')
input_password = ('xpath','//input[@id="password"]')
confirm_password = ('xpath','//input[@id="confirmPassword"]')
submit_button = ('xpath','//button[@type="submit"]')
enter_privat_key = ('xpath','//input[@placeholder="Enter your Private key"]')
button_confirm = ('xpath','//button')
button_confirm2 = ('xpath','//button')
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

        print(f'---------------Akk {index} start---------------')     	

        driver.get(url=rabbi_extension)
        
        try:
            wait.until(ec.visibility_of_element_located((private_key_button))).click()            
        except:
            driver.refresh()
            try:
                wait.until(ec.visibility_of_element_located((private_key_button))).click()
            except Exception as ex:
                driver.save_screenshot('screen.png')
                print(ex)
        
        wait.until(ec.visibility_of_element_located((input_password))).send_keys('12password!')
        
        wait.until(ec.visibility_of_element_located((confirm_password))).send_keys('12password!')
        
        wait.until(ec.visibility_of_element_located((submit_button))).click()
        
        wait.until(ec.visibility_of_element_located((enter_privat_key))).send_keys(privat_key)
        
        wait.until(ec.visibility_of_element_located((button_confirm))).click()
        
        time.sleep(1)
        driver.find_element(*button_confirm2).click()
        time.sleep(2)
        AC(driver).send_keys(Keys.ESCAPE).perform() #"\ue00c"
              
        # time.sleep(2)
        # try:
            # driver.find_element(*pop_up).send_keys(Keys.ESCAPE)
        # except:
        #     driver.refresh()
        #     time.sleep(1)
        #     driver.find_element(*pop_up).send_keys(Keys.ESCAPE)
        # input(1)

# ============================================================================================

        # wait.until(ec.visibility_of_element_located(('xpath','(//div[@class="direction pointer"])[8]'))).click()
        # # //span[text()="Sign"] # вериф после клейма
        # wait.until(ec.visibility_of_element_located(('xpath','//input[@type="text"]'))).send_keys('RUSSIANSF')
        # input(1)
        # wait.until(ec.visibility_of_element_located(('xpath','//button/span[text()="Claim"]'))).click()
        # wait.until(ec.visibility_of_element_located(('xpath','//button/span[text()="Sign and Create"]'))).click()
        # wait.until(ec.visibility_of_element_located(('xpath','//button[text()="Confirm"]'))).click()

# ============================================================================================

        wait.until(ec.visibility_of_element_located((more_btn_9))).click()
        
        wait.until(ec.visibility_of_element_located((gastoken_btn))).click()
        
        # input(1)
        try:
            wait.until(ec.visibility_of_element_located((request_btn))).click()
            time.sleep(1)
            print(f'------------------end--------------------')            

        except:
            wait.until(ec.visibility_of_element_located((Uve_req_2day)))
            print(f'-----------Already requested-------------')

# ============================================================================================
            
        # finally:
        # #     driver.back()
        # #     print('back')
        #     # input(1)
        # wait.until(ec.visibility_of_element_located(('xpath','(//*[local-name()="svg"])[1]'))).click() #'(//*[local-name()="svg" and @class="icon-close brightness-[10]"]'
        # # driver.get(url='chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/popup.html#/dashboard')
        # # input('!!!')
        # # input(2)
        # AC(driver).key_down(Keys.ALT).send_keys('d').key_up(Keys.ALT).perform()
        # # AC(driver).key_up(Keys.ALT).perform()
        # # input(2)
        # AC(driver).key_down(Keys.ALT).send_keys(Keys.ENTER).key_up(Keys.ALT).perform()
        # AC(driver).key_up(Keys.ALT).perform()
        # input(2)
        # wait.until(ec.visibility_of_element_located(('xpath','(//div[@class="direction pointer"])[8]'))).click()
        # # //span[text()="Sign"] # вериф после клейма
        # wait.until(ec.visibility_of_element_located(('xpath','//input[@type="text"]'))).send_keys('RUSSIANSF')
        # wait.until(ec.visibility_of_element_located(('xpath','//button/span[text()="Claim"]'))).click()
        # wait.until(ec.visibility_of_element_located(('xpath','//button/span[text()="Sign and Create"]'))).click()
        # wait.until(ec.visibility_of_element_located(('xpath','//button[text()="Confirm"]'))).click()
        # input(2)

    except Exception as ex:
        # print('???')
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
