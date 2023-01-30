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
from Functions import data, dataNull, Logs_

# Insert icon of web app
icon = Image.open("PetrophysicApp/resources/logo.jpg")
# Page Layout
st.set_page_config(page_title="Well Logs App", page_icon=icon)

# Title of app
st.title("Well Logs Visualization")
st.write("This logs contain information about petrophysical features of any well")

# Upload files
try:
    upload_file_input = st.sidebar.file_uploader("Upload your input LAS file")
    carp_nom = st.sidebar.text_input("Enter the well name")

    if (upload_file_input is not None) and (carp_nom is not None):
        b = "/"
        nomb = str(upload_file_input.name)
        dir = "data/"
        file_name = dir + carp_nom + b + nomb
        file_input = Path(file_name)
        log_input = welly.Well.from_las(file_input)
        df_input = log_input.df()
    elif (upload_file_input is None) and (carp_nom is None):
        st.write("something")
except:
    st.write("Upload a file and enter the well name.")


# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data Information", "Logs Visualization"],
        icons=["house", "clipboard-data", "tv"],
    )


# Call web app sections

if options == "Home":
    st.header("**Well Logs Information**")
    st.write("Well logs are geophysical records of oil and gas well explorations. These logs include detailed information on the geological and physical properties of the subsurface, including depth, resistivity and porosity of rock formations. Well logs are essential for evaluating the production potential of a well and for making informed decisions about drilling and completing the well.")
    img = Image.open("PetrophysicApp/resources/image.png")
    st.image(img,width=100, use_column_width=True)
    video = open("resources/videowelllog.mp4", "rb")
    st.video(video)
    st.caption("Video about Well Logging")



if options == "Data Information":

    try:
        data(df_input)
        dataNull(df_input)
        st.write("Upload a .LAS file")
    except:
        st.write("Upload a file and enter the well name.")



if options == "Logs Visualization":
    try:
        tracks = st.multiselect("Choose the tracks for de plot", df_input.columns)
        d_start = st.number_input("Enter the starting depth", step=1)
        st.caption("Greater depth (ft)")
        d_end = st.number_input("Enter the end depth", step=1)
        st.caption("Shallower depth (ft)")
        Logs_(tracks, log_input, d_end, d_start)
    except:
        st.write("You must enter the depths and choose at least two logs.")
