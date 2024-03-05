#!/usr/bin/env python
# coding: utf-8

# In[57]:


import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.set_page_config(page_title="Air Quality Analysis from Nongzhanguan in 2013-2017")
# Hide PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)
# Load dataset
data = pd.read_csv('datanongzhanguan.csv')
# Title of the dashboard
st.title('Air Quality  Nongzhanguan Station Dashboard')
# Description
st.write('This dashboard focuses on air quality and the variables that affect it as well as the correlation between them.')
# Displaying data statistics
st.subheader('Data Overview for Selected Period')
st.write(data.describe())
fig, axes = plt.subplots(nrows=1, ncols=len(data.columns), figsize=(15, 4))
for i, column in enumerate(data.columns):
    axes[i].hist(data[column])
    axes[i].set_title(column)
st.pyplot(fig)

# Correlation Heatmap
st.subheader('Correlation Heatmap of Air Quality Indicators')
corr = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(corr, annot=True, ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Trend PM2.5 each year
st.subheader('Trend PM2.5 each Year')
fig, ax = plt.subplots(figsize=(10, 6))
trend_pm25 = data.groupby(data['year'])['PM2.5'].mean()
ax.plot(trend_pm25.index, trend_pm25.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Average PM2.5 Level')
st.pyplot(fig)

#Average Pollutant when Rainfall >0
st.subheader('Average Pollutant when Rainfall >0')
rainfall = data[data["RAIN"] > 0]
year_avg_pollutants = rainfall.groupby(rainfall['year'])[['SO2', 'CO', 'NO2', 'O3']].mean()
year_avg_pollutants.plot(kind='line', marker='o')
plt.xlabel('Year')
plt.ylabel('Average Concentration')
plt.legend(title='Pollutants', loc='upper right')
st.pyplot()

# Scatter Plot of PM2.5 vs PM10
st.subheader('Scatter Plot of PM2.5 vs PM10')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='PM2.5', y='PM10', data=data)
plt.xlabel('PM2.5')
plt.ylabel('PM10')
st.pyplot(fig)
