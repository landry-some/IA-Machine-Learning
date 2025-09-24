import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet('taxis.parquet') #pip install pyarrow para ler parquet

df = df[['passenger_count', 'trip_distance', 'RatecodeID', 'PULocationID', 'DOLocationID',
         'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
         'total_amount', 'Airport_fee', 'cbd_congestion_fee']]

df['passenger_count'] = df['passenger_count'].fillna(1)
df.loc[df['passenger_count'] == 0, 'passenger_count'] = 1
df = df[~df['passenger_count'].isin([5, 6, 7, 8, 9])]

df['RatecodeID'] = df['RatecodeID'].fillna(99)
df['Airport_fee'] = df['Airport_fee'].fillna(df['Airport_fee'].mean().round(2))

print(df)