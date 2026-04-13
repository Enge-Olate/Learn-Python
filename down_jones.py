import wget
import zipfile
import os
import pandas as pd
wget.download(
    url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip',
    out='/home/porcupine_ubuntu/Projetos/Backend/Python/Learn-Python/data.zip'
    )

with zipfile.ZipFile(
    './data.zip',
    'r'
) as fp:
    fp.extractall('./data')

os.rename(
    'data/dow_jones_index.data', 
    'data/dow_jones_index.csv'
    )

