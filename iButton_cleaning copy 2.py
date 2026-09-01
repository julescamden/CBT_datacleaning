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
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP3_C.csv"
WP3_C = pd.read_csv(filepath)
WP3_C = WP3_C.rename(columns={'Value': 'Clavicle'})
WP3_C = WP3_C.rename(columns={'Time': 'Date hour'})
WP3_C = WP3_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP3_W.csv"
WP3_W = pd.read_csv(filepath)
WP3_W = WP3_W.rename(columns={'Value': 'Wrist'})
WP3_W = WP3_W.rename(columns={'Time': 'Date hour'})
WP3_W = WP3_W.rename(columns={'Date/Time': 'Date'})

WP3 = pd.merge(WP3_C, WP3_W, how='inner')

# WAKE PERIOD 4
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP4_C.csv"
WP4_C = pd.read_csv(filepath)
WP4_C = WP4_C.rename(columns={'Value': 'Clavicle'})
WP4_C = WP4_C.rename(columns={'Time': 'Date hour'})
WP4_C = WP4_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP4_W.csv"
WP4_W = pd.read_csv(filepath)
WP4_W = WP4_W.rename(columns={'Value': 'Wrist'})
WP4_W = WP4_W.rename(columns={'Time': 'Date hour'})
WP4_W = WP4_W.rename(columns={'Date/Time': 'Date'})

WP4 = pd.merge(WP4_C, WP4_W, how='inner')

# WAKE PERIOD 5
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP5_C.csv"
WP5_C = pd.read_csv(filepath)
WP5_C = WP5_C.rename(columns={'Value': 'Clavicle'})
WP5_C = WP5_C.rename(columns={'Time': 'Date hour'})
WP5_C = WP5_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP5_W.csv"
WP5_W = pd.read_csv(filepath)
WP5_W = WP5_W.rename(columns={'Value': 'Wrist'})
WP5_W = WP5_W.rename(columns={'Time': 'Date hour'})
WP5_W = WP5_W.rename(columns={'Date/Time': 'Date'})

WP5 = pd.merge(WP5_C, WP5_W, how='inner')

# WAKE PERIOD 6
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP6_C.csv"
WP6_C = pd.read_csv(filepath)
WP6_C = WP6_C.rename(columns={'Value': 'Clavicle'})
WP6_C = WP6_C.rename(columns={'Time': 'Date hour'})
WP6_C = WP6_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP6_W.csv"
WP6_W = pd.read_csv(filepath)
WP6_W = WP6_W.rename(columns={'Value': 'Wrist'})
WP6_W = WP6_W.rename(columns={'Time': 'Date hour'})
WP6_W = WP6_W.rename(columns={'Date/Time': 'Date'})

WP6 = pd.merge(WP6_C, WP6_W, how='inner')

# WAKE PERIOD 7
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP7_C.csv"
WP7_C = pd.read_csv(filepath)
WP7_C = WP7_C.rename(columns={'Value': 'Clavicle'})
WP7_C = WP7_C.rename(columns={'Time': 'Date hour'})
WP7_C = WP7_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP7_W.csv"
WP7_W = pd.read_csv(filepath)
WP7_W = WP7_W.rename(columns={'Value': 'Wrist'})
WP7_W = WP7_W.rename(columns={'Time': 'Date hour'})
WP7_W = WP7_W.rename(columns={'Date/Time': 'Date'})

WP7 = pd.merge(WP7_C, WP7_W, how='inner')

# WAKE PERIOD 8
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP8_C.csv"
WP8_C = pd.read_csv(filepath)
WP8_C = WP8_C.rename(columns={'Value': 'Clavicle'})
WP8_C = WP8_C.rename(columns={'Time': 'Date hour'})
WP8_C = WP8_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP8_W.csv"
WP8_W = pd.read_csv(filepath)
WP8_W = WP8_W.rename(columns={'Value': 'Wrist'})
WP8_W = WP8_W.rename(columns={'Time': 'Date hour'})
WP8_W = WP8_W.rename(columns={'Date/Time': 'Date'})

WP8 = pd.merge(WP8_C, WP8_W, how='inner')

# WAKE PERIOD 9
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP9_C.csv"
WP9_C = pd.read_csv(filepath)
WP9_C = WP9_C.rename(columns={'Value': 'Clavicle'})
WP9_C = WP9_C.rename(columns={'Time': 'Date hour'})
WP9_C = WP9_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP9_W.csv"
WP9_W = pd.read_csv(filepath)
WP9_W = WP9_W.rename(columns={'Value': 'Wrist'})
WP9_W = WP9_W.rename(columns={'Time': 'Date hour'})
WP9_W = WP9_W.rename(columns={'Date/Time': 'Date'})

WP9 = pd.merge(WP9_C, WP9_W, how='inner')

# WAKE PERIOD 10
filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP10_C.csv"
WP10_C = pd.read_csv(filepath)
WP10_C = WP10_C.rename(columns={'Value': 'Clavicle'})
WP10_C = WP10_C.rename(columns={'Time': 'Date hour'})
WP10_C = WP10_C.rename(columns={'Date/Time': 'Date'})

filepath = "C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Processed Data/FACT_050/V1/iButtons/FACT_050_V1_WP10_W.csv"
WP10_W = pd.read_csv(filepath)
WP10_W = WP10_W.rename(columns={'Value': 'Wrist'})
WP10_W = WP10_W.rename(columns={'Time': 'Date hour'})
WP10_W = WP10_W.rename(columns={'Date/Time': 'Date'})

WP10 = pd.merge(WP10_C, WP10_W, how='inner')

# Combine all wake periods
df = pd.concat([WP3, WP4, WP5, WP6, WP7, WP8, WP9, WP10])

# Drop rows with no data (there tend to be multiple empty rows at the bottom of these excel sheets)
df = df.dropna(how = 'all')
df = df.query("Clavicle > 22")
df = df.query("Wrist > 22")

# change the 'Date' column from dtype object to dtype datetime64[ns]
#df['Date'] = pd.to_datetime(df['Date'])
#df['Date hour'] = pd.to_datetime(df['Date hour'], format = '%H:%M')

# Create a timestamp column, this will help with calculating elapsed time later on
df['Time Stamp'] = df['Date'].astype(str) + ' ' + df['Date hour'].astype(str)
df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])

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

# create interval averages (this code averages the core temperature for every 10min of data).
# change the 'interval_freq' variable for different time intervals
df = df.reset_index(drop=True)

start_index = df['Time Stamp'].index[0]
end_index = df['Time Stamp'].index[-1]

start_date = df['Time Stamp'].at[start_index]
end_date = df['Time Stamp'].at[end_index]
interval_freq = '10min'  # Hourly intervals

date_intervals = pd.date_range(start=start_date, end=end_date, freq=interval_freq)

hour = pd.DataFrame(columns = ['intervals', 'time', 'date', 'minutes elapsed', 'clavicle', 'wrist'])

for i in range(len(date_intervals) - 1):
    current_interval_start = date_intervals[i]
    current_interval_end = date_intervals[i+1]

    subset_df = df[(df['Time Stamp'] >= current_interval_start) & 
                   (df['Time Stamp'] < current_interval_end)]

    if subset_df.empty:
        continue

    time_index = subset_df.index[0]
    time = subset_df['Date hour'].at[time_index]

    date_index = subset_df.index[0]
    date = subset_df['Date'].at[date_index]

    interval = f"{current_interval_start}, {current_interval_end}"
    
    index = i + 1
    elapsed_time = index*10

    hourly_avg_c = (subset_df.loc[:, 'Clavicle']).mean()
    hourly_avg_w = (subset_df.loc[:, 'Wrist']).mean()
  
    new_row = {"intervals": interval, "time": time, "date": date, "minutes elapsed": elapsed_time, "clavicle": hourly_avg_c, "wrist": hourly_avg_w}

    hour.loc[len(hour)] = new_row

df = hour

# Add WP
WP1 = '7/21/2025'
WP2 = '7/22/2025'
WP3 = '7/23/2025'
WP4 = '7/24/2025'
WP5 = '7/25/2025'
WP6 = '7/26/2025'
WP7 = '7/27/2025'
WP8 = '7/28/2025'
WP9 = '7/29/2025'
WP10 = '7/30/2025'

WP = {WP1: 'WP1', WP2: 'WP2', WP3: 'WP3', WP4: 'WP4', WP5: 'WP5', 
WP6: 'WP6', WP7: 'WP7', WP8: 'WP8', WP9: 'WP9', WP10: 'WP10'}

df['WP'] = df['date'].map(WP)

# Drop variables that won't be necessary for data analysis
df = df.drop(['intervals'], axis = 1)
df['DPG'] = df['wrist'] - df['clavicle']

# Enter the subject ID, should typically be 'FACT_0XX_VX'
sub_id = 'FACT_050_V1'
df['SUBJECT_CODE'] = sub_id

#Rearrange columns
df = df.rename(columns={'time': 'Time', 'date': 'Date', 'minutes elapsed':'Minutes elapsed', 'clavicle': 'Clavicle', 'wrist': 'Wrist'})

df = df[['SUBJECT_CODE', 'Date', 'Time', 'WP', 'Minutes elapsed', 'Clavicle', 'Wrist', 'DPG']]
print(df)

# Convert the dataframe back to a csv file using the file location path. Remember to use the path or else the file will go into the github repo 
# file naming scheme should be 'FACT_0XX_VX_CBT_cleaned' (change for SAM as needed)
df.to_csv("C:/Users/camden/Downloads/FACT_Data_cleaned/iButtons/Cleaned Data/FACT_050/V1/FACT_050_V1_iButtons_cleaned.csv", index = False)