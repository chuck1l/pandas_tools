import pandas as pd
import numpy as np
from read_json import *


# df = pd.read_csv('../collection-master/artwork_data.csv')

# df.to_pickle('../artist_df.pkl')

df = pd.read_pickle('../artist_df.pkl')

n_artist = len(df['artist'].unique())

fb_mask = df['artist'] == 'Bacon, Francis'
num_francis_bacon = df[fb_mask].shape[0]

num_francis_bacon2 = fb_mask.value_counts() # Number true and false

artist_counts = df['artist'].value_counts()
num_francis_bacon3 = artist_counts['Bacon, Francis']

# Utilizing loc and iloc is prefered. No ambiquity.
# Find the area of the artwork
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce') # nan where errors exists in converstion 
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce') # nan where errors exists in converstion 

# add column to pandas df, two methods
area = df['height'] * df['width']
df = df.assign(area=area)
# or 
df['area2'] = df['height'] * df['width']

# what is the biggest artwork in df, by area?
largest_area = df['area'].max()

# return the entire row for that artwork?
print(df.loc[df['area'].idxmax(), : ])
