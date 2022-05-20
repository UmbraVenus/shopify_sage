import streamlit as st
import pandas as pd
import numpy as np
from random import randint

def app():

    st.title("Inventory Tracking App by Sage")
    
    st.write("Reading the first 5 rows from products.csv, data source: https://www.kaggle.com/competitions/grupo-bimbo-inventory-demand/data?select=producto_tabla.csv.zip")
    df = pd.read_csv("products.csv")
    st.dataframe(df.head())
    
    st.markdown("---")
    st.write("Dropping the ID for simplicity")
    df = df.drop(columns="ID")
    st.dataframe(df.head())
    
    st.markdown("---")
    st.write("Adding Quantities because it's inventory management")
    st.caption("Quantities added are randomly generated")
    df["Quantities"] = np.random.randint(0,99, df.shape[0])
    st.dataframe(df.head())
    
    st.markdown("---")
    st.write("Adding warehouse location")
    df["Warehouse ID"] = np.random.randint(1,3, df.shape[0])
    st.dataframe(df.head())
    
    df.to_csv("products_final.csv", index=False)
    
    
    