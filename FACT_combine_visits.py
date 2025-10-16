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

v1 = pd.read_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_048_V1_CBT_ts.csv")
v2 = pd.read_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_048_V2_CBT_ts.csv")

combined = pd.concat([v1, v2])
combined = combined[['SUBJECT_CODE', 'visit', 'hour', 'date', 'time', 'CTEMP', 'intervals']]
combined.to_csv("C:/Users/camden/Downloads/FACT_CBT_cleaned/ts_format/FACT_048_COMBINED_CBT_ts.csv", index = False)