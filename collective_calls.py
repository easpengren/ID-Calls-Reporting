import pandas as pd
file = '/home/ericaspen/Downloads/GAProg_10_09_2020.csv'

df = pd.read_csv(file, sep=',')

print(df)