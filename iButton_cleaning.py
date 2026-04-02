import pandas as pd
import os
import csv
import glob
import sys
import cmath as m
import numpy as np
import statistics as st
import datetime
from datetime import timedelta
from datetime import datetime
import sys
import time

# **BEFORE inputting the data into this script, make sure the csv file has the following features:
# FIVE columns: 'index', 'Date hour' (change to 13:30 Time formatting), 
# 'Date' (copied from the 'Date hour' column and reformatted using Date, m/hh/yyyy), 'Temperature', & 'State' (if the data has already been cleaned, don't include the 'State' variable)
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
filepath = "C:/Users/camden/Downloads/FACT_055_V1_WP3.csv"
df = pd.read_csv(filepath)

df = df[df['Date hour C'] == df['Date hour W']]

df = df.rename(columns={'Date hour C': 'Date hour'})
df = df.drop(['Date hour W'], axis = 1)

# make a df for each iButton in order to make time stamps later
Cdf = df.drop(['Wrist'], axis = 1)
Wdf = df.drop(['Clavicle'], axis = 1)

# Drop rows with no data (there tend to be multiple empty rows at the bottom of these excel sheets)
Cdf = Cdf.dropna(how = 'all')
Wdf = Wdf.dropna(how = 'all')
# change the 'Date' column from dtype object to dtype datetime64[ns]
Cdf['Date'] = pd.to_datetime(Cdf['Date'])
Cdf['Date hour'] = pd.to_datetime(Cdf['Date hour'], format = '%H:%M')

Wdf['Date'] = pd.to_datetime(Wdf['Date'])
Wdf['Date hour'] = pd.to_datetime(Wdf['Date hour'], format = '%H:%M')
# Create a timestamp column, this will help with calculating elapsed time later on
Cdf['Time Stamp'] = Cdf['Date'].astype(str) + ' ' + Cdf['Date hour'].astype(str)
Cdf['Time Stamp'] = pd.to_datetime(Cdf['Time Stamp'])

Wdf['Time Stamp'] = Wdf['Date'].astype(str) + ' ' + Wdf['Date hour'].astype(str)
Wdf['Time Stamp'] = pd.to_datetime(Wdf['Time Stamp'])

#Create the 'elapsed_time_hrs' variable -- this is needed to use the NOSA program
time = Cdf['Time Stamp'].tolist()
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
Cdf['elapsed_time_hrs'] = time_elapsed

time = Wdf['Time Stamp'].tolist()
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
Wdf['elapsed_time_hrs'] = time_elapsed

# create interval averages (this code averages the core temperature for every 10min of data).
# change the 'interval_freq' variable for different time intervals
start_index = Cdf['Time Stamp'].index[0]
end_index = Cdf['Time Stamp'].index[-1]

start_date = Cdf['Time Stamp'].at[start_index]
end_date = Cdf['Time Stamp'].at[end_index]
interval_freq = '10min'  # Hourly intervals

date_intervals = pd.date_range(start=start_date, end=end_date, freq=interval_freq)

hour = pd.DataFrame(columns = ['intervals', 'time', 'date', 'minutes elapsed', 'temp'])

for i in range(len(date_intervals) - 1):
    current_interval_start = date_intervals[i]
    current_interval_end = date_intervals[i+1]

    subset_df = Cdf[(Cdf['Time Stamp'] >= current_interval_start) & 
                   (Cdf['Time Stamp'] < current_interval_end)]

    if subset_df.empty:
        continue

    time_index = subset_df.index[0]
    time = subset_df['Date hour'].at[time_index]

    date_index = subset_df.index[0]
    date = subset_df['Date'].at[date_index]

    interval = f"{current_interval_start}, {current_interval_end}"
    
    index = i + 1
    elapsed_time = index*10

    hourly_avg = (subset_df.loc[:, 'Clavicle']).mean()
  
    new_row = {"intervals": interval, "time": time, "date": date, "minutes elapsed": elapsed_time, "temp": hourly_avg}

    hour.loc[len(hour)] = new_row

print(hour)

start_index = Wdf['Time Stamp'].index[0]
end_index = Wdf['Time Stamp'].index[-1]

start_date = Wdf['Time Stamp'].at[start_index]
end_date = Wdf['Time Stamp'].at[end_index]
interval_freq = '10min'  # Hourly intervals

date_intervals = pd.date_range(start=start_date, end=end_date, freq=interval_freq)

Whour = pd.DataFrame(columns = ['intervals', 'time', 'date', 'minutes elapsed', 'temp'])

for i in range(len(date_intervals) - 1):
    current_interval_start = date_intervals[i]
    current_interval_end = date_intervals[i+1]

    subset_df = Wdf[(Wdf['Time Stamp'] >= current_interval_start) & 
                   (Wdf['Time Stamp'] < current_interval_end)]

    if subset_df.empty:
        continue

    time_index = subset_df.index[0]
    time = subset_df['Date hour'].at[time_index]

    date_index = subset_df.index[0]
    date = subset_df['Date'].at[date_index]

    interval = f"{current_interval_start}, {current_interval_end}"

    index = i + 1
    elapsed_time = index*10

    hourly_avg = (subset_df.loc[:, 'Wrist']).mean()
  
    new_row = {"intervals": interval, "time": time, "date": date, "minutes elapsed": elapsed_time, "temp": hourly_avg}

    Whour.loc[len(Whour)] = new_row

hour = hour.rename(columns={'temp': 'Clavicle'})
hour['Wrist'] = Whour['temp']

df = hour

# Drop variables that won't be necessary for data analysis
df = df.drop(['intervals'], axis = 1)
df['DPG'] = df['Wrist'] - df['Clavicle']

# Enter the subject ID, should typically be 'FACT_0XX_VX'
sub_id = 'FACT_055_V1'
df['SUBJECT_CODE'] = sub_id

#Rearrange columns
df = df.rename(columns={'time': 'Time', 'date': 'Date', 'minutes elapsed':'Minutes elapsed'})

df = df[['SUBJECT_CODE', 'Date', 'Time', 'Minutes elapsed', 'Clavicle', 'Wrist', 'DPG']]
print(df)

# Convert the dataframe back to a csv file using the file location path. Remember to use the path or else the file will go into the github repo 
# file naming scheme should be 'FACT_0XX_VX_CBT_cleaned' (change for SAM as needed)
df.to_csv("C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/FACT_055_V1_WP3_cleaned.csv", index = False)