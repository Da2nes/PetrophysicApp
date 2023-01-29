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
from Functions import data, dataNull

# Insert icon of web app
icon = Image.open("resources/logo.jpg")
# Page Layout
st.set_page_config(page_title="Well Logs App", page_icon=icon)

# Title of app
st.title("Well Logs Visualization")
st.write("This logs contain information about petrophysical features of any well")

# Upload files
upload_file_input = st.sidebar.file_uploader("Upload your input LAS file")
#upload_file_output = st.sidebar.file_uploader("Upload your output LAS file")

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data Information", "Logs Visualization"],
        icons=["house", "clipboard-data", "tv"],
    )

if upload_file_input is not None:
    nomb = str(upload_file_input.name)
    dir = "Data/F1B/"
    file_name = dir+nomb

    file_input = Path(file_name)

    log_input = welly.Well.from_las(file_input)

    df_input = log_input.df()




# Call web app sections
if options == "Data Information":
    data(df_input)
    #data(df_output)
    dataNull(df_input)

if options == "Data Information":
    data(df_input)
    #data(df_output)
    dataNull(df_input)

if options == "Logs Visualization":
    #numTracks = st.number_input("Input track number",step=1)
    st.selectbox("Select",[])


