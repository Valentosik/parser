from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get('http://web.ion.ru/food/FD_tree_grid.aspx')
links = []
div = web.find_element_by_id('Pl_1')
div_res = div.find_element_by_id('TV_1')

i = 643
while i != 1306:
    try:
        result = div_res.find_element_by_id('TV_1n' + str(i))
        result.click()
    except Exception:
        i = i + 1
        continue
    i = i + 1

#links = web.find_elements_by_id('TV_1n' + str(0))
#for i in range(len(links)):
    #links[i].click()