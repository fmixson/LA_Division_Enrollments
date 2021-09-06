from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome("C:/Users/family/PycharmProjects/chromedriver.exe")
driver.get('https://secure.cerritos.edu/schedule/')
check_all = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[1]/label/input').click()
check_LA = driver.find_element_by_xpath('/html/body/form/b/b/table[4]/tbody/tr[5]/td[2]/label/input').click()
click_View_Divisions = driver.find_element_by_xpath('/html/body/form/b/b/p[2]/input').click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'AFRS105descs')))
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
courses_td = soup.find_all(['table', 'bgcolor'])
# print(courses_td)
for table in courses_td:
    # print('this is table',table)
    print()
    print()
    # tr_table = table.find_all('tr')
    # print('this is tr table', tr_table)
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols=[x.text.strip() for x in cols]
        if len(cols) == 17:
            print(len(cols))
            print(cols)
    print()
    print()
    # for tr in tr_table:
    #     print(tr)
    # print()
    # print()
