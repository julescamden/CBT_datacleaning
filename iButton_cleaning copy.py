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
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP3_C.csv"
WP3_C = pd.read_csv(filepath)
WP3_C = WP3_C.rename(columns={'Date hour C': 'Date hour'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP3_W.csv"
WP3_W = pd.read_csv(filepath)
WP3_W = WP3_W.rename(columns={'Date hour W': 'Date hour'})

WP3 = pd.merge(WP3_C, WP3_W, how='inner')

# WAKE PERIOD 4
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP4_C.csv"
WP4_C = pd.read_csv(filepath)
WP4_C = WP4_C.rename(columns={'Date hour C': 'Date hour'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP4_W.csv"
WP4_W = pd.read_csv(filepath)
WP4_W = WP4_W.rename(columns={'Date hour W': 'Date hour'})

WP4 = pd.merge(WP4_C, WP4_W, how='inner')

# WAKE PERIOD 5
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP5_C.csv"
WP5_C = pd.read_csv(filepath)

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP5_W.csv"
WP5_W = pd.read_csv(filepath)

WP5 = pd.merge(WP5_C, WP5_W, how='inner')

# WAKE PERIOD 6
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP6_C.csv"
WP6_C = pd.read_csv(filepath)

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP6_W.csv"
WP6_W = pd.read_csv(filepath)

WP6 = pd.merge(WP6_C, WP6_W, how='inner')

# WAKE PERIOD 7
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP7_C.csv"
WP7_C = pd.read_csv(filepath)

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP7_W.csv"
WP7_W = pd.read_csv(filepath)

WP7 = pd.merge(WP7_C, WP7_W, how='inner')

# WAKE PERIOD 8
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP8_C.csv"
WP8_C = pd.read_csv(filepath)

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP8_W.csv"
WP8_W = pd.read_csv(filepath)

WP8 = pd.merge(WP8_C, WP8_W, how='inner')

# WAKE PERIOD 9
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP9_C.csv"
WP9_C = pd.read_csv(filepath)

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP9_W.csv"
WP9_W = pd.read_csv(filepath)

WP9 = pd.merge(WP9_C, WP9_W, how='inner')

# WAKE PERIOD 10
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP10_C.csv"
WP10_C = pd.read_csv(filepath)

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_054/V1/FACT_054_V1_WP10_W.csv"
WP10_W = pd.read_csv(filepath)

WP10 = pd.merge(WP10_C, WP10_W, how='inner')

# Combine all wake periods

df = pd.concat([WP3, WP4, WP5, WP6, WP7, WP8, WP9, WP10])
print(df)

# make a df for each iButton in order to make time stamps later
Cdf = df.drop(['Wrist'], axis = 1)
Wdf = df.drop(['Clavicle'], axis = 1)

# Drop rows with no data (there tend to be multiple empty rows at the bottom of these excel sheets)
Cdf = Cdf.dropna(how = 'all')
Wdf = Wdf.dropna(how = 'all')
# change the 'Date' column from dtype object to dtype datetime64[ns]
Cdf['Date'] = pd.to_datetime(Cdf['Date'])
Wdf['Date'] = pd.to_datetime(Wdf['Date'])

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

hour = hour.rename(columns={'temp': 'Wrist'})
hour['Wrist'] = Whour['temp']

df = hour
print(df)
sys.exit()
# Add WP
WP1 = '2025-07-07'
WP2 = '2025-07-08'
WP3 = '2025-07-09'
WP4 = '2025-07-10'
WP5 = '2025-07-11'
WP6 = '2025-07-12'
WP7 = '2025-07-13'
WP8 = '2025-07-14'
WP9 =  '2025-07-15'
WP10 = '2025-07-16'

WP = {WP1: 'WP1', WP2: 'WP2', WP3: 'WP3', WP4: 'WP4', WP5: 'WP5', 
WP6: 'WP6', WP7: 'WP7', WP8: 'WP8', WP9: 'WP9', WP10: 'WP10'}

df['WP'] = df['Date'].map(WP)
# Drop variables that won't be necessary for data analysis
df = df.drop(['intervals'], axis = 1)
df['DPG'] = df['Wrist'] - df['Clavicle']

# Enter the subject ID, should typically be 'FACT_0XX_VX'
sub_id = 'FACT_054_V1'
df['SUBJECT_CODE'] = sub_id

#Rearrange columns
df = df.rename(columns={'time': 'Time', 'date': 'Date', 'minutes elapsed':'Minutes elapsed'})

df = df[['SUBJECT_CODE', 'Date', 'Time', 'WP', 'Minutes elapsed', 'Clavicle', 'Wrist', 'DPG']]
print(df)

# Convert the dataframe back to a csv file using the file location path. Remember to use the path or else the file will go into the github repo 
# file naming scheme should be 'FACT_0XX_VX_CBT_cleaned' (change for SAM as needed)
#df.to_csv("C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/FACT_055_V1_WP3_cleaned.csv", index = False)