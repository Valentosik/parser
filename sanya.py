from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def recurcion(s):
    m = True
    try:
        s.click()
        return m
    except Exception:
        m = False
        print('Error')
        return m


web = webdriver.Chrome('/Users/aleksandrgorbunov/PycharmProjects/parser/chromedriver')
web.get('http://web.ion.ru/food/FD_tree_grid.aspx')
links = []
div = web.find_element_by_xpath('//div[@id="TV_1"]').find_elements_by_xpath('//a[contains(@id, "TV_1n")]')
i = 0
print(div)
while i < len(div):
    while True:
        m = recurcion(div[i])
        if m == True:
            break
        else:
            recurcion(div[i])
    i = i + 1
a_div = web.find_elements_by_xpath('//a[contains(@class, "TV_1_0 TV_1_1 TV_1_7")]')
print(len(a_div))
names_of_products = []
for j in a_div:
    names_of_products.append(j.text)
inf_products = []
for h in a_div:
    time.sleep(2)
    h.click()
    table_inf = web.find_element_by_xpath('//div[contains(@id, "Pl_2")]').find_element_by_tag_name('tbody').find_elements_by_tag_name('td')
    for k in table_inf:
        print(k.text)


for a in inf_products:
    print(a)

