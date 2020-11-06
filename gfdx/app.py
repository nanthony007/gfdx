import time
import json
import datetime
import random

import streamlit as st


with open("data/logs.json") as f:
    logs = json.load(f)


def run_analysis() -> None:
    """Calls a series of modular functions in succession.

    This function calls other modules from the analysis package
    in succession to update the GFDx REDCAP database.

    Raises:
        ValueError: ValueError raised if analysis fails.

    Returns:
        None
    """
    raise ValueError


st.set_page_config(
    page_title="GFDx Analysis",
    layout="centered",
)

"""
## Welcome to the GFDx Streamlit webapp.
---
To manually run the analysis click the button below. \
Please be patient and do not refresh the page, it may take a while.

If you have any concerns or if more than one recent run has failed \
    you should contact Nick Anthony at nanthony007@gmail.com.
"""

if st.button(
    "Run Analysis",
):
    with st.spinner("Running analysis..."):
        time.sleep(2)

        try:
            run_analysis()

            logs.append(
                {
                    "result": "Success",
                    "timestamp": str(datetime.datetime.now()),
                }
            )

            with open("data/logs.json", "w") as f:
                json.dump(logs, f)

            st.success("Analysis Complete.")

        # will need to change specfic exception
        except ValueError:
            st.error("Analysis Failed.")