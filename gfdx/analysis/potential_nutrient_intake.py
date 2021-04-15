# -*- coding: utf-8 -*-
"""Potential Nutrient Intake.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/107j9j8FvTv9WRSWEZMyJv1uODpyJFbl_

## Potential Nutrient intake
"""

# Install package to allow import from REDCap API
from redcap import Project
import pandas as pd
import numpy as np
import os
from tqdm.notebook import tqdm  # progress bar

# Connecting to GFDx Redcap API

api_key = os.environ.get("APIKEY")


# Connecting to GFDx Redcap API
URL = "https://redcap.emory.edu/api/"
project = Project(URL, api_key)

# Pulls out variables of interest
fields_of_interest = [
    "country_code",
    "nutrient_level",
    "latest_intake_api",
    "ip_pc_api",
    "compliance_pc_api",
    "standard_nutrient",
]
subset = project.export_records(fields=fields_of_interest, format="df")

# Reset index
df = subset
df.reset_index(inplace=True)

df = df[df.country_code != 999.0]  # Remove country code 999

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
df2 = df[df.redcap_event_name.isin(food_list)]
df1 = df2[df.redcap_repeat_instrument == "nutrients_compounds"]

df_copy1 = df1

# 1. Nutrient Intake
def intake_pc(row):
    try:
        return float(row.nutrient_level) / 1000 * (float(row.latest_intake_api))
    except ValueError:
        return "Not enough data to calculate"


df_copy1["nutrient_intake"] = df_copy1.apply(lambda row: intake_pc(row), axis=1)

# 2. Nutrient Intake, Adjusted
def intake_adj_pc(row):
    if row.nutrient_intake == "Not enough data to calculate":
        return "Not enough data to calculate"
    else:
        try:
            return (
                float(row.nutrient_intake)
                * (float(row.ip_pc_api) / 100)
                * (float(row.compliance_pc_api) / 100)
            )
        except ValueError:
            return "Not enough data to calculate"


df_copy1["nutrient_intake_adj"] = df_copy1.apply(lambda row: intake_adj_pc(row), axis=1)

# 3. EAR
def ear_pc(row):
    if row.nutrient_intake == "Not enough data to calculate":
        return "Not enough data to calculate"
    elif row.standard_nutrient == 1:
        try:
            return float(row.nutrient_intake) / 1.1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 2:
        try:
            return float(row.nutrient_intake) / 0.002 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 3:
        try:
            return float(row.nutrient_intake) / 800 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 4:
        try:
            return float(row.nutrient_intake) / 3 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 5:
        try:
            return float(row.nutrient_intake) / 0.4 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 6:
        try:
            return float(row.nutrient_intake) / 0.095 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 7:
        try:
            return float(row.nutrient_intake) / 8.1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 8:
        try:
            return float(row.nutrient_intake) / 11 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 9:
        try:
            return float(row.nutrient_intake) / 0.9 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 10:
        try:
            return float(row.nutrient_intake) / 0.045 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 11:
        try:
            return float(row.nutrient_intake) / 0.9 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 12:
        try:
            return float(row.nutrient_intake) / 0.5 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 13:
        try:
            return float(row.nutrient_intake) / 0.01 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 14:
        try:
            return float(row.nutrient_intake) / 12 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 15:
        try:
            return float(row.nutrient_intake) / 6.8 * 100
        except ValueError:
            return "Not enough data to calculate"


df_copy1["nutrient_ear_pc"] = df_copy1.apply(lambda row: ear_pc(row), axis=1)

# 3. EAR, Adjusted
def ear_adj_pc(row):
    if row.nutrient_intake_adj == "Not enough data to calculate":
        return "Not enough data to calculate"
    elif row.standard_nutrient == 1:
        try:
            return float(row.nutrient_intake_adj) / 1.1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 2:
        try:
            return float(row.nutrient_intake_adj) / 0.002 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 3:
        try:
            return float(row.nutrient_intake_adj) / 800 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 4:
        try:
            return float(row.nutrient_intake_adj) / 3 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 5:
        try:
            return float(row.nutrient_intake_adj) / 0.4 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 6:
        try:
            return float(row.nutrient_intake_adj) / 0.095 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 7:
        try:
            return float(row.nutrient_intake_adj) / 8.1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 8:
        try:
            return float(row.nutrient_intake_adj) / 11 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 9:
        try:
            return float(row.nutrient_intake_adj) / 0.9 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 10:
        try:
            return float(row.nutrient_intake_adj) / 0.045 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 11:
        try:
            return float(row.nutrient_intake_adj) / 0.9 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 12:
        try:
            return float(row.nutrient_intake_adj) / 0.5 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 13:
        try:
            return float(row.nutrient_intake_adj) / 0.01 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 14:
        try:
            return float(row.nutrient_intake_adj) / 12 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 15:
        try:
            return float(row.nutrient_intake_adj) / 6.8 * 100
        except ValueError:
            return "Not enough data to calculate"


df_copy1["nutrient_ear_pc_adj"] = df_copy1.apply(lambda row: ear_adj_pc(row), axis=1)

# 5. UL
def ul_pc(row):
    if (
        row.standard_nutrient == 2
        or row.standard_nutrient == 9
        or row.standard_nutrient == 11
    ):
        return "No UL for this nutrient"
    elif row.nutrient_intake == "Not enough data to calculate":
        return "Not enough data to calculate"
    elif row.standard_nutrient == 1:
        try:
            return float(row.nutrient_intake) / 100 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 3:
        try:
            return float(row.nutrient_intake) / 2500 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 4:
        try:
            return float(row.nutrient_intake) / 10 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 5:
        try:
            return float(row.nutrient_intake) / 1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 6:
        try:
            return float(row.nutrient_intake) / 0.6 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 7:
        try:
            return float(row.nutrient_intake) / 45 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 8:
        try:
            return float(row.nutrient_intake) / 35 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 10:
        try:
            return float(row.nutrient_intake) / 0.04 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 12:
        try:
            return float(row.nutrient_intake) / 3 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 13:
        try:
            return float(row.nutrient_intake) / 0.1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 14:
        try:
            return float(row.nutrient_intake) / 1000 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 15:
        try:
            return float(row.nutrient_intake) / 40 * 100
        except ValueError:
            return "Not enough data to calculate"


df_copy1["nutrient_ul_pc"] = df_copy1.apply(lambda row: ul_pc(row), axis=1)

# 6. UL, Adjusted
def ul_adj_pc(row):
    if (
        row.standard_nutrient == 2
        or row.standard_nutrient == 9
        or row.standard_nutrient == 11
    ):
        return "No UL for this nutrient"
    elif row.nutrient_intake_adj == "Not enough data to calculate":
        return "Not enough data to calculate"
    elif row.standard_nutrient == 1:
        try:
            return float(row.nutrient_intake_adj) / 100 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 3:
        try:
            return float(row.nutrient_intake_adj) / 2500 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 4:
        try:
            return float(row.nutrient_intake_adj) / 10 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 5:
        try:
            return float(row.nutrient_intake_adj) / 1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 6:
        try:
            return float(row.nutrient_intake_adj) / 0.6 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 7:
        try:
            return float(row.nutrient_intake_adj) / 45 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 8:
        try:
            return float(row.nutrient_intake_adj) / 35 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 10:
        try:
            return float(row.nutrient_intake_adj) / 0.04 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 12:
        try:
            return float(row.nutrient_intake_adj) / 3 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 13:
        try:
            return float(row.nutrient_intake_adj) / 0.1 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 14:
        try:
            return float(row.nutrient_intake_adj) / 1000 * 100
        except ValueError:
            return "Not enough data to calculate"
    elif row.standard_nutrient == 15:
        try:
            return float(row.nutrient_intake_adj) / 40 * 100
        except ValueError:
            return "Not enough data to calculate"


df_copy1["nutrient_ul_pc_adj"] = df_copy1.apply(lambda row: ul_adj_pc(row), axis=1)

final = df_copy1

final.drop(["nutrient_level"], axis=1, inplace=True)
final.drop(["latest_intake_api"], axis=1, inplace=True)
final.drop(["ip_pc_api"], axis=1, inplace=True)
final.drop(["compliance_pc_api"], axis=1, inplace=True)
final.drop(["standard_nutrient"], axis=1, inplace=True)

final["country_code"] = final.country_code.apply(lambda x: int(x))
final["redcap_repeat_instance"] = final.redcap_repeat_instance.apply(lambda x: int(x))

# Formats data into acceptable table for import into REDCap
final2 = final.set_index(["country_code", "redcap_event_name"])

# FINAL IMPORT - Import to REDCap through API
project.import_records(final2)