# Script to randomly sample the data

# Import packages
import pandas as pd
from crime_categories import crime_categories

# Read the full data
df = pd.read_csv('data/la_crime_2020_2024_full.csv', sep=",")

### REDUCE DATA
# Randomly sample 200000 observations from the original data
df_sample = df.sample(n=200000, random_state=2)

# Drop unnecessary columns and data
df_sample = df_sample.drop(columns=['AREA','Rpt Dist No', 'Part 1-2', 'Crm Cd','Mocodes','Premis Cd','Weapon Used Cd','Status', 'Cross Street'])
df_sample = df_sample[df_sample['Date Rptd'].str.contains('2024') == False]

# Insert crime categories
# Function to categorize crimes based on the crime categories dictionary
def categorize_crime(crime):
    for category, crimes in crime_categories.items():
        if crime in crimes:
            return category
    return 'OTHER'  # For crimes that don't fall into the defined categories

# Apply the function to each row in the dataset and create a new column 'crime category'
df_sample['Category'] = df_sample['Crm Cd Desc'].apply(categorize_crime)

# Reorder the columns
new_order = [
    'DR_NO', 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA NAME', 'Crm Cd Desc', 'Category',
    'Vict Age', 'Vict Sex', 'Vict Descent', 'Premis Desc', 'Weapon Desc', 'Status Desc',
    'Crm Cd 1', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'LOCATION', 'LAT', 'LON'
]
df_sample = df_sample[new_order]

# Export the sampled data into a csv file
df_sample.to_csv('data/la_crime_2020_2024_reduced.csv', index=False)  

### FILTER OUT SENSITIVE CASES
## Remove all cases where the victim age ranges between 0 and 18
df_safe = df_sample[(df_sample["Vict Age"] > 18) | (df_sample["Vict Age"] < 0)]

## Remove all cases that contains sensitive crime description
# Words to check for
words = ['child', 'sex', 'rape', 'chld', 'animal', 'philia', 'minor']

# Use str.contains with a regular expression to match any of the words
pattern = '|'.join(words)  # Create a pattern with | as the separator
df_safe = df_sample[df_sample['Crm Cd Desc'].str.contains(pattern, case=False) == False]

# Export the sampled data into a csv file
df_safe.to_csv('data/la_crime_2020_2024_safe.csv', index=False)  


