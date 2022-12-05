import time
import olx_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

links, prices, addresses = olx_data.get_olx_data()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("C:/Users/Jakub/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get(olx_data.FORM_LINK)


time.sleep(2)
for i in range(len(links)):
    address_textbox = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_textbox = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price_textbox = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    adres_to_be_sent = addresses[i]
    link_to_be_sent = links[i]
    price_to_be_sent = prices[i]

    print(adres_to_be_sent, link_to_be_sent, price_to_be_sent)

    address_textbox.send_keys(adres_to_be_sent)
    link_textbox.send_keys(link_to_be_sent)
    price_textbox.send_keys(price_to_be_sent)

    send_button.click()
    driver.get(olx_data.FORM_LINK)
    time.sleep(2)

