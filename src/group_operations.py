import pandas as pd
import numpy as np

df = pd.read_pickle('../artist_df.pkl')


grouped = df.groupby('artist')

