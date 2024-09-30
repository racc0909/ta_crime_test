import pandas as pd

df = pd.read_csv('data/la_weather_2020_2024_original.csv', sep=',')

# Drop unwanted columns
df_new = df.drop(columns=['name', 'precip','precipprob','precipcover','preciptype','sealevelpressure','severerisk','stations'])

df_new['datetime'] = pd.to_datetime(df_new['datetime'], format='%Y-%m-%d')
df_new['sunrise'] = pd.to_datetime(df_new['sunrise'], format="%Y-%m-%dT%H:%M:%S")
df_new['sunset'] = pd.to_datetime(df_new['sunset'], format="%Y-%m-%dT%H:%M:%S")


df_new.info()



# Export cleaned data as a new csv
df_new.to_csv('data/la_weather_2020_2024_cleaned.csv', index=False)