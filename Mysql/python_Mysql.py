# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:16:45 2024

@author: Shin
"""

# [connections.my_database]
type="sql"
dialect="mysql"
username="shin"
password="1234"
host="localhost" # IP or URL
port=3306 # Port number
database="extinction" # Database name
    
import streamlit as st

conn = st.connection("extinction")  
df = conn.query("SELECT * FROM extinction.cofog_health")
st.dataframe(df)
#%%
import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
