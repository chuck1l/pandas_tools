import pandas as pd
import numpy as np
import json
import os

keys_to_use = [
    'id', 'all_artists', 'title', 'medium', 'dateText',
    'acquisitionYear', 'height', 'width', 'units'
]

def get_record_from_file(file_path, keys_to_use):
    '''
    Process a single JSON file and return a tuple with
    the desired fields
    '''
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)

    record = []
    for field in keys_to_use:
        record.append(content[field])

    return tuple(record)

# Look at the first file to get an idea of the data format
sample_json = os.path.join('..', 'collection-master', 'artworks', 'a',
                           '000', 'a00001-1035.json')

sample_record = get_record_from_file(sample_json, keys_to_use)

def read_artworks_from_json(keys_to_use):
    '''
    Traverse all of the directories with JSON files within the
    original root as specided by JSON_ROOT path. This case we 
    are only extracting the first file with "break" to minimize 
    compuation. Don't use break in real-life scenario.
    '''
    JSON_ROOT = os.path.join('..', 'collection-master', 'artworks')

    artworks = []
    for root, _, files in os.walk(JSON_ROOT):
        for f in files:
            if f.endswith('json'):
                PATH = os.path.join(root, f)
                record = get_record_from_file(PATH, keys_to_use)
                artworks.append(record)
            break
    df = pd.DataFrame.from_records(artworks, columns=keys_to_use, index='id')

    return df

# other case might be wiser to specify root and pass in as an argument, this
# case the root was built into the function

df = read_artworks_from_json(keys_to_use)



