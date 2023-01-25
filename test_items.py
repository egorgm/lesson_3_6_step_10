import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def test_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30) #Такое длинное ожидание добавлено в соответствии с критериями
    assert browser.find_elements(By.CSS_SELECTOR,'#add_to_basket_form > button1'),'Кнопка добавления товара в корзину отсутствует'
    