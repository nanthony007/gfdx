import streamlit as st
import pandas as pd
import datetime
import time

st.beta_set_page_config(
    page_title="GFDx Analysis",
    layout="centered",
)

st.title("Welcome to the GFDx Streamlit webapp.")
st.text("THIS IS NEW")
st.subheader(
    "This table shows the most recent five runs of the program and their result status."
)
st.write("To manually run the analysis click the button below.")


slot1 = st.empty()
slot2 = st.empty()

df = pd.read_csv("data/executions.csv")

main_table = st.table(df.tail())


def get_result(x=True):
    return "Success" if x else "Fail"


def update_data():
    with st.spinner("Analysis running..."):
        time.sleep(5)
    result = get_result()
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%b-%d-%Y %H:%M:%S")
    execution_dict = {
        "Result": result,
        "Timestamp": formatted_time,
    }
    added = df.append(execution_dict, ignore_index=True)
    main_table.add_rows(added.tail(1))
    added.to_csv("gfdx_analysis/executions.csv", index=False)
    st.info("Analysis complete.  See table for result status.")
    return True


if slot1.button(
    "Update",
):
    update_data()
