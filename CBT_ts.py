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
import math
import timedelta


# load data
filepath = "C:/Users/camden/Downloads/SAM_CBT_cleaned/SAM_028_CBT_cleaned.csv"
df = pd.read_csv(filepath)

# re-add the 'Time Stamp' variable
df['Time Stamp'] = df['Date'].astype(str) + ' ' + df['Date hour'].astype(str)
df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])

# filter out temperature values hat are not physiologically possible
df = df.drop(df.loc[df['CTEMP'] < 36.00].index)

# sorry for the hard coding D:
# define each WP date. add more for SAM as needed
start_study_date = '2025-07-07'
WP2 = '2025-07-08'
WP3 = '2025-07-09'
WP4 = '2025-07-10'
WP5 = '2025-07-11'
WP6 = '2025-07-12'
WP7 = '2025-07-13'
WP8 = '2025-07-14'
WP9 =  '2025-07-15'
WP10 = '2025-07-16'
WP11 = '2025-07-17'
WP12 = '2025-07-18'
WP13 = '2025-07-19'
end_study_date = '2025-07-20'

WP = {start_study_date: 'WP1', WP2: 'WP2', WP3: 'WP3', WP4: 'WP4', WP5: 'WP5', 
WP6: 'WP6', WP7: 'WP7', WP8: 'WP8', WP9: 'WP9', WP10: 'WP10', WP11: 'WP11', WP12: 'WP12', WP13: 'WP13', end_study_date: 'WP14'}

df['WP'] = df['Date'].map(WP)

# create interval averages (this code averages the core temperature for every 10min of data).
# change the 'interval_freq' variable for different time intervals
start_index = df['Time Stamp'].index[0]
end_index = df['Time Stamp'].index[-1]

start_date = df['Time Stamp'].at[start_index]
end_date = df['Time Stamp'].at[end_index]
interval_freq = '30min'  # Hourly intervals

date_intervals = pd.date_range(start=start_date, end=end_date, freq=interval_freq)

hour = pd.DataFrame(columns = ['intervals', 'time', 'date', 'hour', 'CTEMP', 'WP'])

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

    elapsed_time = i

    hourly_avg = (subset_df.loc[:, 'CTEMP']).mean()
  
    new_row = {"intervals": interval, "time": time, "date": date, "hour": elapsed_time, "CTEMP": hourly_avg}

    hour.loc[len(hour)] = new_row

#add the wake period
hour['WP'] = hour['date'].map(WP)
print(hour)
#reformat the data for R analysis
ok = pd.pivot_table(hour, index = ['time'], columns = ['WP'], values = ['CTEMP'])

#format column names
ok.columns = ['_'.join(str(s).strip() for s in col if s) for col in ok.columns]

#reset index
ok.reset_index(inplace=True)

#remove 'CTEMP_' prefix 
ok.columns = [col.replace('CTEMP_', '') for col in ok.columns]

ok = ok[['time', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7', 'WP8', 'WP9', 'WP10', 'WP11', 'WP12', 'WP13', 'WP14']]
print(ok)

#sub_id = 'FACT_048_V1'
#hour['SUBJECT_CODE'] = sub_id

'''
#For FACT only
visit = 'V1'
hour['visit'] = visit
hour = hour[['SUBJECT_CODE', 'visit', 'hour', 'date', 'time', 'CTEMP', 'intervals']]
'''

# Save the data to a csv file
#ok.to_csv("C:/Users/camden/Downloads/SAM_CBT_cleaned/ts_format/SAM_028_CBT_ts_30min.csv", index = False)
