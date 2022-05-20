import streamlit as st
st.set_page_config(layout="wide")

from multiapp import MultiApp
# import apps here
import reference
# comment placeholder
import inventory
import datapre

# initiate multiple app sidebar interface
app = MultiApp()

# add apps here, order matters
app.add_app("Inventory Management", inventory.app)
app.add_app("Data Pre-Processing(before writing this app)", datapre.app)
app.add_app("Reference", reference.app)

# run apps
app.run()