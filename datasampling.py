# Script to randomly sample the data

# Import packages
import pandas as pd

# Read the full data
df = pd.read_csv('data/la_crime_2020_2024_full.csv', sep=",")


### REDUCE DATA
# Randomly sample 200000 observations from the original data
df_sample = df.sample(n=200000, random_state=2)

# Export the sampled data into a csv file
df_sample.to_csv('data/la_crime_2020_2024_reduced.csv', index=False)  

### FILTER OUT SENSITIVE CASES
## Remove all cases where the victim age ranges between 0 and 18
df_safe = df_sample[(df_sample["Vict Age"] > 18) | (df_sample["Vict Age"] < 0)]

## Remove all cases that contains sensitive crime description
# Words to check for
words = ['child', 'sex', 'rape']

# Use str.contains with a regular expression to match any of the words
pattern = '|'.join(words)  # Create a pattern with | as the separator
df_safe = df_sample[df_sample['Crm Cd Desc'].str.contains(pattern, case=False) == False]

# Export the sampled data into a csv file
df_safe.to_csv('data/la_crime_2020_2024_safe.csv', index=False)  


