from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Whatsapp:
    def find_element(self, driver, xpath, timeout: int = 300):
        while timeout > 0:
            try:
                return driver.find_element_by_xpath(xpath).click()
            except:
                time.sleep(1)
                timeout -= 1
        raise RuntimeError(f"Page loading timeout")

    def send_message(self, driver, xpath, messages, timeout: int = 300):
        while timeout > 0:
            try:
                for m in messages:
                    inputElement = driver.find_element_by_xpath(xpath)
                    inputElement.send_keys(m)
                    self.find_element(driver, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
                return
            except:
                time.sleep(1)
                timeout -= 1
        raise RuntimeError(f"Page loading timeout")

    def Browser(self, number, messages):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=C:\Users\gabri\Desktop\Carson\selenium\data")

        driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)

        driver.get('https://wa.me/'+number)

        self.find_element(driver, '//*[@id="action-button"]')
        self.find_element(driver, '/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a')

        self.send_message(driver, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', messages)

        time.sleep(3)
        driver.close()