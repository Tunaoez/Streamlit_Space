import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


# Draw a title and some text to the app:
st.title("People in Space & ISS Current Location")
st.header("This app provides an overview about people who are in _space_ righ now as well as their current location")

#people in space
space = requests.get("http://api.open-notify.org/astros.json/")
data = json.loads(space.text)
nr = data["number"]

# number
st.subheader("Number of people")
st.write(str(nr))

# name
st.subheader("Name of people")
for item in data["people"]:
    st.write((item["name"]))

# -------------------------PLOT SIMPLE MAP----------------------------

# Location
url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)
# df

# Create new column called latitude and longitude and drop index and message
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True) 
df = df.drop(['index', 'message'], axis=1)
# df

# Plot 
fig = px.scatter_geo(data_frame=df, lat='latitude', lon='longitude')
#fig.show()
st.plotly_chart(fig, use_container_width=True)

st.subheader("Current ISS Location (refresh to update)")

if st.checkbox('view data'):
    st.subheader('Raw Data')
    st.write(df)

st.map(df)
