import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing

st.title('house price prediction using ML')
st.image('https://cdn.dribbble.com/userupload/23217976/file/original-203940eb89dec42ee25f6af662af24dc.gif')
df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]
st.sidebar.title('Select house feature')
st.sidebar.image('https://cdn.dribbble.com/userupload/23217976/file/original-203940eb89dec42ee25f6af662af24dc.gif')
all_value = []
for i in X:
  mi_value = int(X[i].min())
  max_value = int(X[i].max())
  
  ans = st.sidebar.slider(f'Select {i} value',min_value,max_value)
  all_value.append(ans)
#st.write(all_value)


