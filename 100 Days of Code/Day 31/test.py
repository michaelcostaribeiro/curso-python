import pandas
from random import choice


DATA_LOCATION = 'data/french_words.csv'

data = pandas.read_csv(DATA_LOCATION)

print(data['French'].tolist())
print(len(data['French'].tolist()))
