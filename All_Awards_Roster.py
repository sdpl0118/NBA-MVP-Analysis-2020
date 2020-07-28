# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 09:08:48 2020

@author: user
"""
import requests
from lxml import etree
import os, time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import pandas as pd 
browser = webdriver.Firefox(executable_path=r'D:/bteststat/geckodriver.exe')
#r = requests.get(url).text
#s = etree.HTML(r)

"""
url = 'https://www.basketball-reference.com/leagues/NBA_*SEASON*.html'
browser.get(url)
data = browser.find_element_by_id("div_all-nba")
test = data.text
test
pathstr = 'D:/bteststat/' + 'testingallstar' + ".csv"
f = open(pathstr, "w", encoding="utf-8")
f.write(test)
"""

# grab All NBA Teams,all_all-defensive,allstar,allrookie (buggy due to ads on site, but works)
scrapeBbalRef(2000, 2019, 'https://www.basketball-reference.com/leagues/NBA_*SEASON*.html','all_star_game_rosters','D:/bteststat/AllstarNew', False)

def scrapeBbalRef(year_start, year_end, page_string, id, folder_name, toggle_partial = True ):
    for season in range(year_start, year_end+1):
        #print(season)
        # navigate to bballref
        url = page_string.replace("*SEASON*", str(season))
        browser.get(url)

        # grab raw CSV (div_all-defensive, div_all-nba, div_all-rookie,div_all_star_game_rosters)
        data = browser.find_element_by_id("div_all_star_game_rosters")
        List = data.text

        # write to CSV
        pathstr = folder_name + "/" + str(season) + ".csv"
        f = open(pathstr, "w", encoding="utf-8")
        f.write(List)

