# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:09:18 2020

@author: user
"""

import os, time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox(executable_path=r'D:/bteststat/geckodriver.exe')
wait = WebDriverWait(browser, 15)

# grab ROY stats (buggy, but works)
scrapeBbalRef(2011, 2019, 'https://www.basketball-reference.com/awards/awards_*SEASON*.html','all_roy','D:/bteststat/roy-award-stats', False)

def scrapeBbalRef(year_start, year_end, page_string, id, folder_name, toggle_partial = True ):
    for season in range(year_start, year_end+1):
        #print(season)
        # navigate to bballref
        url = page_string.replace("*SEASON*", str(season))
        browser.get(url)

        # setup id strings
        #partial_id = id + "_toggle_partial_table"
        #csv_id = "csv_" + id

        # activate and grab data in CSV format
        #if toggle_partial:
            #browser.execute_script('document.getElementById("'+ partial_id +'").click();')

        # grab raw CSV
        item = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='all_roy']/div[1]/div/ul/li[1]/span")))
        item.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='all_roy']/div[1]/div/ul/li[1]/div/ul/li[4]/button"))).click()
        raw_csv = browser.execute_script('''var content = document.getElementById("csv_roy")
            return content.textContent
            ''')

        #print(raw_csv)
        # write to CSV
        pathstr = folder_name + "/" + str(season) + ".csv"
        f = open(pathstr, "w", encoding="utf-8")
        f.write(raw_csv)
