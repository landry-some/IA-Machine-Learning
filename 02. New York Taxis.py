import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lista = []

df = pd.read_parquet('taxis.parquet') #pip install pyarrow para ler parquet

df = df[['passenger_count', 'trip_distance', 'RatecodeID', 'PULocationID', 'DOLocationID',
         'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
         'total_amount', 'Airport_fee', 'cbd_congestion_fee']]

print(df.isna().sum())

df['passenger_count'] = df['passenger_count'].fillna(1)
df['RatecodeID'] = df['RatecodeID'].fillna(99)
df['Airport_fee'] = df['Airport_fee'].fillna(df['Airport_fee'].mean().round(2))

print(df)