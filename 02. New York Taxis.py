import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet('taxis.parquet') #pip install pyarrow para ler parquet

df = df[['passenger_count', 'trip_distance', 'RatecodeID', 'PULocationID', 'DOLocationID',
         'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
         'improvement_surcharge','total_amount', 'Airport_fee', 'congestion_surcharge',
         'cbd_congestion_fee']]

df['passenger_count'] = df['passenger_count'].fillna(1)
df.loc[df['passenger_count'] == 0, 'passenger_count'] = 1
df = df[df['passenger_count'] <= 5]

df['RatecodeID'] = df['RatecodeID'].fillna(99)
df['Airport_fee'] = df['Airport_fee'].fillna(0)

df['congestion_surcharge'] = df['congestion_surcharge'].fillna(2.50)
df = df[(df['congestion_surcharge'] >= 0.0) & (df['fare_amount'] >= 0.0)
        & (df['extra'] >= 0.0) & (df['mta_tax'] >= 0.0) & (df['tip_amount'] >= 0.0)
        & (df['tolls_amount'] >= 0.0) & (df['improvement_surcharge'] >= 0.0)
        & (df['total_amount'] >= 0.0) & (df['Airport_fee'] >= 0.0)
        & (df['cbd_congestion_fee'] >= 0.0)]

print(df)