# -*- coding: utf-8 -*-
"""monitoring.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C1RrFwlocAxdZ-08wRLje8ws1gk-asb2

## Monitoring: country has all protocols which are applicable?
"""


import os

import numpy as np
import pandas as pd

# Install package to allow import from REDCap API
from redcap import Project
from tqdm.notebook import tqdm  # progress bar

api_key = os.environ.get("APIKEY")


# Connecting to GFDx Redcap API
URL = "https://redcap.emory.edu/api/"
project = Project(URL, api_key)

# Pulls out variables of interest from REDCap in table format
fields_of_interest = [
    "country_code",
    "status_food",
    "emp_applicability",
    "ext_mon_protocol",
    "imp_applicability",
    "imp_mon_protocol",
]
subset = project.export_records(fields=fields_of_interest, format="df")

# Reset index
df = subset.copy()
df.reset_index(inplace=True)

# remove invalid country code
df = df[df.country_code != 999.0]

# Pulls out the specific food vehicles of interest
# Saves in new table
food_list = [
    "maize_flour_arm_1",
    "wheat_flour_arm_1",
    "rice_arm_1",
    "salt_arm_1",
    "oil_arm_1",
    "maize_flour_arm_2",
    "wheat_flour_arm_2",
    "rice_arm_2",
    "salt_arm_2",
    "oil_arm_2",
]
df1 = df[df.redcap_event_name.isin(food_list)]

# External should and does
def external(row):
    if (
        (row.emp_applicability == 1 and row.ext_mon_protocol == 1)
        or (row.emp_applicability == 2 and row.ext_mon_protocol == 2)
        or (row.emp_applicability == 2 and row.ext_mon_protocol == 3)
    ):
        return 1
    else:
        return 2


df1["external_s_d"] = df1.apply(lambda row: external(row), axis=1)

# Import should and does
def internal(row):
    if (
        (row.imp_applicability == 1 and row.imp_mon_protocol == 1)
        or (row.imp_applicability == 2 and row.imp_mon_protocol == 2)
        or (row.imp_applicability == 2 and row.imp_mon_protocol == 3)
    ):
        return 1
    else:
        return 2


df1["import_s_d"] = df1.apply(lambda row: internal(row), axis=1)

# Protocol should and does
def protocol(row):
    if row.external_s_d == 1 and row.import_s_d == 1:
        return 1
    else:
        return 2


df1["protocol_s_d"] = df1.apply(lambda row: protocol(row), axis=1)

# Create the final dataset to import to REDCap by dropping variables - only upload variables created
df1.drop(
    [
        "status_food",
        "emp_applicability",
        "ext_mon_protocol",
        "imp_applicability",
        "imp_mon_protocol",
    ],
    axis=1,
    inplace=True,
)

# Change the country code to integer form
df1["country_code"] = df1.country_code.apply(lambda x: int(x))

# Formats data into acceptable table for import into REDCap
df1.set_index(["country_code", "redcap_event_name"], inplace=True)

# FINAL IMPORT - Import to REDCap through API
project.import_records(df1)
