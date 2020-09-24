import pandas as pd
from pprint import pprint

df = pd.read_csv("gfdx.csv")
pprint(df.head(), indent=4)

pprint(df.shape)