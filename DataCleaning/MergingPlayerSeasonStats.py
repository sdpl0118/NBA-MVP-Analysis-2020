# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:45:56 2020

@author: user
"""
import pandas as pd
import numpy as np

#Input Variables
PlayerListYOY(1983, 2020, "D:/bteststat/season-stats-pergame/*SEASON*.csv")

#Forloop Function that merges data files
def PlayerListYOY(year_start, year_end, FilePath):
    for season in range(year_start, year_end+1):
        File = FilePath.replace("*SEASON*", str(season))
        df = pd.read_csv(File)
        
        #replacing 'NaN' with '0' in % columns
        df = df.replace(np.nan,0)

        #Adding Year of Stats
        df["Year"] = str(season)
        
        #Saving via append
        df.to_csv('D:/bteststat/PlayerSeasonStatsCombined.csv', mode='a', header=False)

#reopening the file        
df1 = pd.read_csv('D:/bteststat/PlayerSeasonStatsCombined.csv')

#Checking the Column Names
df1.columns.values

#Cleaning Special Char
df1.Player = df1.Player.str.replace(r"[^a-zA-Z\_\' '\-\č\ć\\\\]+", "")

#Fixing incorrect column name
df1.rename(columns = {'1983':'Year'},inplace=True)

#Removing duplicating headers
df1.drop_duplicates(subset=['Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'],keep=False,inplace=True) 

#Splitting Player name from String
df1[['PlayerName','PlayerID']]=df1.Player.str.split('\\',expand=True)

#Sorting columns
df1 = df1[[ 'Year', 'PlayerName', 'PlayerID', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']]
