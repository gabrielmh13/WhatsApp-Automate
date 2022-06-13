from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import pathlib

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

    def verify_sent(self, driver, messages, timeout: int = 300):
        xpath1 = "//div[@class='_22Msk' and contains(., '" + messages[len(messages)-1][0] + "') and contains(.//@data-pre-plain-text, '" + datetime.today().strftime('%d/%m/%Y') + "') and contains(.//@aria-label, 'Enviada')]"
        xpath2 = "//div[@class='_22Msk' and contains(., '" + messages[len(messages)-1][0] + "') and contains(.//@data-pre-plain-text, '" + datetime.today().strftime('%d/%m/%Y') + "') and contains(.//@aria-label, 'Entregue')]"
        xpath3 = "//div[@class='_22Msk' and contains(., '" + messages[len(messages)-1][0] + "') and contains(.//@data-pre-plain-text, '" + datetime.today().strftime('%d/%m/%Y') + "') and contains(.//@aria-label, 'Lida')]"
        while timeout > 0:
            try:
                driver.find_element_by_xpath(xpath1)
                print('Message Sent! - Enviada')
                return
            except:
                try:
                    driver.find_element_by_xpath(xpath2)
                    print('Message Sent! - Entregue')
                    return
                except:
                    try:
                        driver.find_element_by_xpath(xpath3)
                        print('Message Sent! - Lida')
                        return
                    except:
                        time.sleep(1)
                        timeout -= 1
        raise RuntimeError(f"Page loading timeout")

    def browser(self, numbers, db):
        options = webdriver.ChromeOptions()
        datadir = str(pathlib.Path(__file__).parent.resolve()) + '\data'
        options.add_argument(r"user-data-dir="+datadir)

        if(len(numbers) > 0):
            driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)

            for number in numbers:
                messages = db.execQuery("SELECT msg FROM mensagens WHERE cel = '" + number[0] + "' AND fk_data = '" + datetime.today().strftime('%Y%m%d') + "'")

                driver.get('https://wa.me/'+number[0])

                self.find_element(driver, '//*[@id="action-button"]')
                self.find_element(driver, '/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a')

                self.send_message(driver, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', messages)

                self.verify_sent(driver, messages)
                db.update("UPDATE mensagens SET status = 1 WHERE cel = '" + number[0] + "' AND fk_data = '" + datetime.today().strftime('%Y%m%d') + "'")

               
            driver.close()