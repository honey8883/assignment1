import sys
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

output_xpath = '//*[@id="sciOutPut"]'

input_xpath = '//*[@id="sciInPut"]'

number_xpaths = {
    1:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[1]',
    2:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]',
    3:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]',
    4:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]',
    5:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[2]',
    6:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[3]',
    7:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[1]',
    8:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[2]',
    9:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[3]',
    0:'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]',
}

def internal_click_plus(driver):
    driver.find_element(By.XPATH,'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[4]').click()


def internal_click_minus(driver):
    driver.find_element(By.XPATH,'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()


def internal_click_mul(driver):
    driver.find_element(By.XPATH,'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[4]').click()


def internal_click_div(driver):
    driver.find_element(By.XPATH,'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[4]').click()

def internal_click_percent(driver):
    driver.find_element(By.XPATH,'//*[@id="sciout"]/tbody/tr[2]/td[1]/div/div[5]/span[4]').click()

def internal_click_neg(driver):
    driver.find_element(By.XPATH,'//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[1]').click()

def internal_click_digit(driver,digit):
    driver.find_element(By.XPATH,number_xpaths[digit]).click()


def internal_wait_for_content(driver):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "contentout")))
        

def test_multiplication():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # load URL
        chrome_driver.get('https://www.calculator.net')
        
        # wait for the website to load
        internal_wait_for_content(chrome_driver)
        
        calc_output = chrome_driver.find_element(By.XPATH,output_xpath)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_mul(chrome_driver)
        internal_click_digit(chrome_driver,5)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,5)
        assert(calc_output.text.strip() == "222075")
    finally:
        chrome_driver.close()



def test_division():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # load URL
        chrome_driver.get('https://www.calculator.net')
        
        # wait for the website to load
        internal_wait_for_content(chrome_driver)
        
        calc_output = chrome_driver.find_element(By.XPATH,output_xpath)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,0)
        internal_click_digit(chrome_driver,0)
        internal_click_digit(chrome_driver,0)
        internal_click_div(chrome_driver)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,0)
        internal_click_digit(chrome_driver,0)
        assert(calc_output.text.strip() == "20")
    finally:
        chrome_driver.close()

def test_addition():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # load URL
        chrome_driver.get('https://www.calculator.net')
        
        # wait for the website to load
        internal_wait_for_content(chrome_driver)
        
        calc_output = chrome_driver.find_element(By.XPATH,output_xpath)
        internal_click_neg(chrome_driver)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_digit(chrome_driver,4)
        internal_click_plus(chrome_driver)
        internal_click_digit(chrome_driver,3)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,5)
        internal_click_digit(chrome_driver,3)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,5)
        assert(calc_output.text.strip() == "111111")
    finally:
        chrome_driver.close()

def test_substraction():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # load URL
        chrome_driver.get('https://www.calculator.net')
        
        # wait for the website to load
        internal_wait_for_content(chrome_driver)
        
        calc_output = chrome_driver.find_element(By.XPATH,output_xpath)
        
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,8)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_minus(chrome_driver)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_digit(chrome_driver,0)
        internal_click_digit(chrome_driver,9)
        internal_click_digit(chrome_driver,4)
        internal_click_digit(chrome_driver,8)
        internal_click_digit(chrome_driver,2)
        internal_click_digit(chrome_driver,3)
        internal_click_neg(chrome_driver)

        assert(calc_output.text.strip() == "23329646")
    finally:
        chrome_driver.close()