# Import Libraries
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



def data(dataframe):
    st.header("**Dataframe header**")
    st.write(dataframe.head())
    st.header("**Statistical information**")
    st.write(dataframe.describe())

def dataNull(dataframe):
    st.header("**Null Data Resume**")
    df_n = dataframe.isna().sum()
    df_n = pd.DataFrame(df_n)
    st.write(df_n)
    #fig_n = plt.bar(df_n.index,df_n[0])
    st.bar_chart(df_n)

def Logs_(curvas, log, inicio, final):
    fig2, axes = plt.subplots(1, len(curvas), figsize=(20, 10))
    for ind, curva in enumerate(curvas):
        segmento = log.data[curva].to_basis(start=inicio, stop=final)
        if curva == 'SAND_FLAG':
            segmento.plot_2d(ax=axes[ind])
        else:
            segmento.plot(ax=axes[ind])
        axes[ind].set_title(curva)
    axes[0].set_ylabel('Depth (m)', fontsize=14)
    fig2.suptitle('Petrophysical Logs', fontsize=16)
    st.pyplot(fig=fig2)



