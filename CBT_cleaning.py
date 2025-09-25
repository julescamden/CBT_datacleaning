import pandas as pd
import os
import csv
import glob
import sys
import cmath as m
import numpy as np
import statistics as st
import datetime
import sys

# input the directory to the CBT_cleaned CSV file
filepath = "C:/Users/camden/Downloads/FACT_054_V1_CBT - Copy(in).csv"
df = pd.read_csv(filepath)

# define the start/end dates for the in-lab
start = '9/3/2025'
end = '9/12/2025'

# change the 'Date' column from dtype object to dtype datetime64[ns]
df['Date'] = pd.to_datetime(df['Date'])

# create a variable with only the correct in-lab date range
correct_range = (df['Date'] >= start) & (df['Date'] <= end)

df['CorrectDate'] = correct_range

# drop all rows that are not from the in-lab
df = df.drop(df[df.CorrectDate == False].index)

# drop all rows that have no temperature data
df = df.drop(df[df.State == 'Sync'].index)

# drop rows that won't be needed for future analysis
df = df.drop(['State', 'CorrectDate'], axis = 1)

# sort dates chronologically
df = df.sort_values(by = 'Date')

# convert the dataframe back to a csv file using the file location path. 
# file naming scheme should be 'FACT_0XX_VX_CBT_cleaned' (change for SAM as needed)
df.to_csv("C:/Users/camden/Downloads/FACT_054_V1_CBT_cleaned.csv", index = False, )