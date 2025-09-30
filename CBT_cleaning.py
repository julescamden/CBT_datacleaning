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
import time

# **BEFORE inputting the data into this script, make sure the csv file has the following features:
# FIVE columns: 'index', 'Date hour' (change to 13:30 Time formatting), 
# 'Date' (copied from the 'Date hour' column and reformatted using Date, m/hh/yyyy), 'Temperature', & 'State' (if the data has already been ceaned, don't include the 'State' variable)
# Make sure there are no spaces in front of variable names

#The original csv will allocate different saved pdfs of data into different columns. 
# manually move ALL 'Temperature' and 'State' columns into only two columns

#Delete all blocks of text in the file that are unrelated to the data inputs

# Make sure pandas is downloaded. If you do not have pandas (an error will appear when you run the script if you don't have this package), 
# type 'pip install pandas' into the python terminal.
# create a file called 'requirements.txt' in the same location as this script.
# Once pandas is downloaded, type 'pip freeze > requirements.txt' to store your packages

def get_duration(duration):
    hours = int(duration / 3600)
    minutes = int(duration % 3600 / 60)
    seconds = int((duration % 3600) % 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

# input the directory to the CBT_Reorganized CSV file
filepath = "C:/Users/camden/Downloads/FACT_048_V1_CBT"
df = pd.read_csv(filepath)

# define the start/end dates for the in-lab
start = '11/04/2024'
end = '11/13/2024'

# Drop rows with no data (there tend to be multiple empty rows at the bottom of these excel sheets)
df = df.dropna(how = 'all')

# change the 'Date' column from dtype object to dtype datetime64[ns]
df['Date'] = pd.to_datetime(df['Date'])

# Create a timestamp column, this will help with calculating elapsed time later on
df['Time Stamp'] = df['Date'].astype(str) + ' ' + df['Date hour'].astype(str)
df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])

# create a variable with only the correct in-lab date range
correct_range = (df['Date'] >= start) & (df['Date'] <= end)

df['CorrectDate'] = correct_range

# drop all rows that are not from the in-lab
df = df.drop(df[df.CorrectDate == False].index)

# drop all rows that have no temperature data -- comment this out if the variable was not included
df = df.drop(df[df.State == 'Sync'].index)

# drop rows that won't be needed for future analysis -- comment this out if the variable was not included
df = df.drop(['State', 'CorrectDate'], axis = 1)

# sort dates chronologically
df = df.sort_values(by = ['Date', 'Date hour'])

#Create the 'elapsed_time_hrs' variable -- this is needed to use the NOSA program
time = df['Time Stamp'].tolist()
time_elapsed = [0]
for i in range(1, len(time)):
    # Calling the current index time and subtracting it by the first timestamp recorded for the data
    start = time[0]
    finish = time[i]
    duration = (finish - start).total_seconds()

    # Calculating how many hours have passed between the current time and the first recorded time
    elapsed_hours = get_duration(duration)

    # Converting time elapsed to a decimal
    hours, minutes, seconds = elapsed_hours.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    result = hours + (minutes / 60) + (seconds / 3600)
    time_elapsed.append(result)

# Create the hours elapsed variable -- variable name should not be changed from what is already provided
df['elapsed_time_hrs'] = time_elapsed

# Drop variables that won't be necessary for data analysis
df = df.drop(['Time Stamp', 'index'], axis = 1)
df = df.rename(columns = {'Temperature':'CTEMP'})

# Enter the subject ID, should typically be 'FACT_0XX_VX'
sub_id = 'FACT_048_V1'
df['SUBJECT_CODE'] = sub_id

#Rearrange columns
df = df[['SUBJECT_CODE', 'Date', 'Date hour', 'CTEMP', 'elapsed_time_hrs']]

# Convert the dataframe back to a csv file using the file location path. Remember to use the path or else the file will go into the github repo 
# file naming scheme should be 'FACT_0XX_VX_CBT_cleaned' (change for SAM as needed)
df.to_csv("C:/Users/camden/Downloads/CBT_cleaned/FACT_048_V1_CBT_cleaned.csv", index = False)