from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
import data
import json


class MST:
    def __init__(self):
        self.login = 'data.login'
        self.password = 'data.password'

    def get_log_pas(self):
        with open("config.txt", 'r') as file:
            index = 0
            for line in file:
                if index == 0:
                    self.login = line
                    index += 1
                if index == 1:
                    self.password = line

    def auth(self):
        MST.get_log_pas(self)
        options = Options_chrome()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get('https://mstnw.net/')
        btn_auth = driver.find_element_by_xpath('/html/body/header/div/div/div/div[2]/button')
        btn_auth.click()
        insert_login = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div/div/input[6]')
        insert_login.send_keys(self.login)
        insert_password = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div/div/input[7]')
        insert_password.send_keys(self.password)
        btn_continue = driver.find_element_by_xpath('//*[@id="install_allow"]')
        btn_continue.click()
        btn_user = driver.find_element_by_xpath('/html/body/header/div/div/div/div[3]/div/a')
        btn_user.click()
        btn_card = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/img')
        btn_card.click()


run = MST()
run.auth()
