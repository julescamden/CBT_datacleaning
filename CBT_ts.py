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

#load data
filepath = "C:/Users/camden/Downloads/FACT_CBT_cleaned/FACT_050_V2_CBT_cleaned.csv"
df = pd.read_csv(filepath)

#re-add the 'Time Stamp' variable
df['Time Stamp'] = df['Date'].astype(str) + ' ' + df['Date hour'].astype(str)
df['Time Stamp'] = pd.to_datetime(df['Time Stamp'])

end_study_date = '2025-09-22'

start_index = df['Time Stamp'].index[0]
end_index = df['Time Stamp'].index[-1]

start_date = df['Time Stamp'].at[start_index]
end_date = df['Time Stamp'].at[end_index]
interval_freq = '1H'  # Hourly intervals

date_intervals = pd.date_range(start=start_date, end=end_date, freq=interval_freq)

hour = pd.DataFrame(columns = ['intervals', 'time', 'date', 'hour', 'CTEMP'])

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

    interval = f"{current_interval_start} to {current_interval_end}"

    elapsed_time = i

    hourly_avg = (subset_df.loc[:, 'CTEMP']).mean()
  
    new_row = {"intervals": interval, "time": time, "date": date, "hour": elapsed_time, "CTEMP": hourly_avg, }

    hour.loc[len(hour)] = new_row

sub_id = 'FACT_050_V2'
hour['SUBJECT_CODE'] = sub_id

visit = 'V2'
hour['visit'] = visit
#hour.to_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_050_V2_CBT_ts.csv", index = False)

#hour = hour[['SUBJECT_CODE', 'visit', 'hour', 'date', 'time', 'CTEMP', 'intervals']]

#Combine V1 and V2 data for analysis

v1 = pd.read_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_050_V1_CBT_ts.csv")
v2 = pd.read_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_050_V2_CBT_ts.csv")

combined = pd.concat([v1, v2])
combined = combined[['SUBJECT_CODE', 'visit', 'hour', 'date', 'time', 'CTEMP', 'intervals']]
combined.to_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_050_COMBINED_CBT_ts.csv", index = False)
