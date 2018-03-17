import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
#open("/home/ramesh/Downloads/international-football-results-from-1872-to-2017.zip")
from_csv = pd.read_csv("/home/ramesh/Downloads/international-football-results-from-1872-to-2017.zip")
print(from_csv.head())# .head for reading first 5 rows data

#cols=['date',"tournnament","city","cournty","home_team","away_team","home_score","away_score"]
no_header=pd.read_csv("/home/ramesh/Downloads/international-football-results-from-1872-to-2017.zip")
print(no_header.head())
print(no_header.info())
print(no_header.dtypes)
print(no_header.describe())