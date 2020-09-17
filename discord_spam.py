from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import sys
import os
from googletrans import Translator

class discordbot:
    def __init__(self, email, password):
        self.email = email
        self.password  = password
        options = Options()
        options.headless = True
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        GOOGLE_CHROME_PATH = os.environ['GOOGLE_CHROME_PATH']
        CHROMEDRIVER_PATH = os.environ['CHROMEDRIVER_PATH']
        options.binary_location = GOOGLE_CHROME_PATH
        self.driver = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, options=options)
        print('Headless Chrome Should Work Now')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.discord.com/login/')
        time.sleep(2)
        email_elem = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
        email_elem.send_keys(self.email)
        password_elem = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        
        driver.get(os.environ['LINK'])
        time.sleep(5)

    def spam(self):
        print('spam is being used')
        driver = self.driver
        type_elem = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')
        list_of_langs = ['Bangla', 'Hindi', 'Italian', 'French', 'Japanese', 'Korean', 'Russian', 'Punjabi', 'Spanish', 'Swedish', 'Latin', 'Urdu', 'Tamil', 'Telugu', 'Thai', 'Malayalam', 'Nepali', 'Gujarati', 'Greek', 'German']
        translator = Translator()
        I_love_you = translator.translate('I love you', dest=random.choice(list_of_langs)).text
        type_elem.send_keys('Fady, ' + I_love_you)
        type_elem.send_keys(Keys.RETURN)
        time.sleep(120)

if __name__ == "__main__":

    email = os.environ['EMAIL']
    password = os.environ['PASSWORD']

    disco = discordbot(email, password)
    disco.login()

    while True:
        try:
            disco.spam()
        except Exception as e:
            print(e)
            disco.closeBrowser()
            time.sleep(60)
            disco = discordbot(email, password)
            disco.login()
