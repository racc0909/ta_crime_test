# Script to randomly sample the data

# Import packages
import pandas as pd

# Read the full data
df = pd.read_csv('data/la_crime_2020_present_full.csv', sep=",")

# Randomly sample 200000 observations from the original data
df_sample = df.sample(n=200000, random_state=2)

# Export the sampled data into a csv file
df_sample.to_csv('data/la_crime_2020_2024_reduced.csv', index=False)  