# -*- coding: utf-8 -*-
"""Foundational Documents.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fWj5TOjmKMY_kw8-BK5trtyM3gXInJo5
"""

import os

import numpy as np
import pandas as pd
# Install package to allow import from REDCap API
from redcap import Project
from tqdm.notebook import tqdm  # progress bar

api_key = os.environ.get("APIKEY")  # NICK API ADDED HERE PLEASE FIX


# Connecting to GFDx Redcap API
URL = "https://redcap.emory.edu/api/"
project = Project(URL, api_key)

# Pulls out variables of interest from REDCap in table format
fields_of_interest = [
    "country_code",
    "mf_comment",
    "mf_original_source_english",
    "ls_types_comment_english",
    "ls_source_english",
    "ls_origins_comment_english",
    "ls_uses_comment_english",
]
subset = project.export_records(fields=fields_of_interest, format="df")

# Reset index, removes multi-index
df = subset.copy()
df.reset_index(inplace=True)

# remove invalid country code
df = df[df.country_code != 999.0]

final = df  # Rename dataframe

# Create fields of interest
final["e1_comment"] = df.mf_comment
final["e1_source"] = df.mf_original_source_english
final["e2a_text"] = df.ls_types_comment_english
final["e2a_source"] = df.ls_source_english
final["e2b_text"] = df.ls_origins_comment_english
final["e2b_source"] = df.ls_source_english
final["e2c_text"] = df.ls_uses_comment_english
final["e2c_source"] = df.ls_source_english

# Drop fields not needed for import
final.drop(
    [
        "mf_comment",
        "mf_original_source_english",
        "ls_types_comment_english",
        "ls_origins_comment_english",
        "ls_source_english",
        "ls_uses_comment_english",
    ],
    axis=1,
    inplace=True,
)

# Change the country code to integer form
final["country_code"] = final.country_code.apply(lambda x: int(x))

# Formats data into acceptable table for import into REDCap
final.set_index(["country_code", "redcap_event_name"], inplace=True)

# FINAL IMPORT - Import to REDCap through API
project.import_records(final)
