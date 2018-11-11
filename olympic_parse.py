import pandas as pd
import csv

df = pd.read_csv("athlete_events.csv", na_values = ['no info', '.'])

df.sort_values('Year')

print (df.head(100))