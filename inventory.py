import streamlit as st
import pandas as pd
import numpy as np

def app():

    st.title("Inventory Tracking App by Sage")
    st.markdown("---")
    st.write("Product Catalog(first 5 only):")
    df = pd.read_csv("products_final.csv")
    st.dataframe(df.head())
    st.write("Warehouse Catalog(first 5 only)")
    warehouse = pd.read_csv("warehouse.csv")
    st.dataframe(warehouse.head())
    
    # =================
    # Adding an item
    # =================
    st.markdown("---")
    st.header("Adding an item here:")
    with st.form("Add an item here:"):
        st.write("Input the item name, then input the quantities, and Warehouse ID")
        input_name = st.text_input("Input name here")
        input_quan = st.number_input("Input quantities here")
        input_warehouse = st.selectbox('Select Warehouse Location Here', warehouse["Warehouse ID"].unique())

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("You have inputted "+str(input_quan)+" of "+input_name)
            df.loc[len(df.index)] = [input_name, int(input_quan), input_warehouse]
            df.to_csv("products_final.csv", index=False)
    
    # =================
    # editing an item
    # =================
    st.markdown("---")
    st.header("Edit an item here:")
    with st.form("Select the row you want to edit here:"):
        input_row = st.text_input("Input the item name here")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("You have selected: ")
            st.write(df.loc[df['Name']==input_row])
        
    with st.form("Edit an item here:"):
        st.write("Edit the item name, then edit the quantities and Warehouse ID")
        
        input_name = st.text_input("Input name here")
        input_quan = st.number_input("Input quantities here")
        input_warehouse = st.selectbox('Select Warehouse Location Here', warehouse["Warehouse ID"].unique())

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("You have inputted "+str(input_quan)+" of "+input_name)
            df.loc[df['Name']==input_row] = [input_name, int(input_quan), input_warehouse]
            df.to_csv("products_final.csv", index=False)
    
    # =================
    # Deleting an item
    # =================
    st.markdown("---")
    st.header("Delete an item here:")
    with st.form("Select the row you want to delete here:"):
        input_row = st.text_input("Input the item name here")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("You have selected: ")
            st.write(df.loc[df['Name']==input_row])
            df = df.drop(df.index[df['Name']==input_row])
            st.dataframe(df.head())
            df.reset_index(inplace=True)
            df.to_csv("products_final.csv", index=False)
    
    # =================
    # Adding an warehouse
    # =================
    st.markdown("---")
    st.header("Extra Credit! :D")
    st.header("Adding an warehouse here:")
    with st.form("Add a warehouse here:"):
        st.write("Input the Warehouse ID, then the warehouse Name")
        input_name = st.text_input("Input name here")
        input_id = st.number_input("Input ID here")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("You have inputted warehouse "+str(input_id)+" of "+input_name)
            warehouse.loc[len(warehouse.index)] = [input_name, int(input_id)]
            st.dataframe(warehouse)
            df.to_csv("warehouse.csv", index=False)
    
    # =================
    # Viewing a whole list
    # =================
    st.markdown("---")
    st.header("Viewing a whole list")
    st.dataframe(df)
            
            
    