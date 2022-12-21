## Generate Sample Data with Faker ##

import os
import pandas as pd
from faker import Faker
from csv import DictReader, DictWriter

## Generate 100 fake profiles
fake = Faker()
profiles = []
for _ in range(100):
    new_profile = fake.profile()
    new_profile['birthdate'] = str(new_profile['birthdate'])
    new_profile['current_location'] = ', '.join([str(item) for item in new_profile['current_location']])
    new_profile['website'] = ' '.join(new_profile['website'])
    profiles.append(new_profile)
column_names = list(profiles[0].keys())    

## Save the data into the csv file
new_dir = os.getcwd() + '/data/'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

with open('data/Profiles.csv', 'w+') as file:
    fieldnames = column_names
    writer = DictWriter(file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    
    for item in profiles:
        writer.writerow(item)

## Check if data is the same
data = pd.read_csv('./data/Profiles.csv', delimiter='\t')
profiles_df = pd.DataFrame(profiles)
print(data.equals(profiles_df))
