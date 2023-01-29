# Import python libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import welly
import lasio
from streamlit_option_menu import option_menu
from PIL import Image
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')
from Code.Functions import data

# Insert icon of web app
icon = Image.open("resources/logo.jpg")
# Page Layout
st.set_page_config(page_title="Well Logs App", page_icon=icon)

# Title of app
st.title("Well Logs Visualization")
st.write("This logs contain information about petrophysical features of any well")

# Upload files
upload_file_input = st.sidebar.file_uploader("Upload your input LAS file")
upload_file_output = st.sidebar.file_uploader("Upload your output LAS file")

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data Information", "Logs Visualization"],
        icons=["house", "clipboard-data", "tv"],
    )

#DataFrame
file_input = upload_file_input
file_output = upload_file_output
log_input = welly.well.from_las(file_input)
log_output = welly.well.from_las(file_output)
df_input = pd.DataFrame(log_input)
df_output = pd.DataFrame(log_output)




# Call dataframe
if upload_file_input:
    df_input
if upload_file_output:
    df_output

# Call web app sections
if options == "Data Information":
    data(df_input)
    data(df_output)

