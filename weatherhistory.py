import streamlit as st
import pandas as pd
import numpy as np

#Title
st.title('Weather History Dashboard')

#Loading dataset
weatherhistory = pd.read_csv('weatherHistory.csv')
weatherhistory.head()

#Header
st.header('Weather History Data in Szeged 2006-2016')

#Caption
st.caption('The dataset includes a hourly/daily summary for Szeged, Hungary area, between 2006 and 2016. Link to the dataset: https://www.kaggle.com/code/rtatman/regression-challenge-day-1/data')

#Codeblock
code = '''def weatherHistory():
    print("Weather History Dashboard")'''
st.code(code, language='python')

#Dataframe 1 and Chart 1
st.subheader('Weather Visualization; Barchart')
Summary = weatherhistory['Summary'].value_counts()
st.bar_chart(Summary)
st.caption('This barchart visualizes the weather patterns counts')
#Dataframe 2 and Chart 2
st.subheader('Humidity trends; Line Chart')
Humidity = weatherhistory['Humidity']
st.line_chart(Humidity)
st.caption('This line chart shows the humidity trends over the years')