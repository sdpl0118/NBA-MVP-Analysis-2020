# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:15:49 2020

@author: user
"""
import pandas as pd

#Create a new CSV file for previously scraped data
df = pd.DataFrame(list())
df.rename(columns={0: 'id', 1: 'PlayerName',2: 'AllStarStatus'}, inplace=True)
df.to_csv('D:/bteststat/AllstarList.csv')

#Input Variables
AllstarListYOY(2000, 2020, "D:/bteststat/AllstarNew/*SEASON*.csv")

#Forloop Function that merges data files
def AllstarListYOY(year_start, year_end, FilePath):
    for season in range(year_start, year_end+1):
        File = FilePath.replace("*SEASON*", str(season))
        df = pd.read_csv(File)
        
        #Cleaning Column Names
        df = df.rename(columns={'East': 'PlayerName','Giannis': 'PlayerName','LeBron': 'PlayerName','Stephen': 'PlayerName'})
        df = df[~df.PlayerName.str.contains('West')]
        
        #Adding Year of Allstar and Allstar Status
        df["Year"] = str(season)
        df["AllStar"] = "1"
        
        #Cleaning Special Char & Saving via append
        df.PlayerName = df.PlayerName.str.replace(r"[^a-zA-Z\_\' '\č\ć]+", "")
        df.to_csv('D:/bteststat/AllstarList.csv', mode='a', header=False)
#Checkcheck
#pd.read_csv('D:/bteststat/AllstarList.csv')
