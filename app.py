import streamlit as st
import requests as r
import pandas as pd
import json

st.title('My title')
st.header('My header')
st.subheader('My sub')

baseUrl = "https://extranet.who.int/publicemergency/api/Monkeypox/CaseSummary"
rawData = r.post(baseUrl)
rawData = rawData.json()

df = pd.DataFrame(rawData["Data"])
df = df.replace(r'^s*$', float('NaN'), regex = True)
newDf = df.dropna(axis=0, subset=['ISO3'])

st.json(rawData)
st.dataframe(df)
st.write(df.info())
st.dataframe(newDf)
st.write(newDf.info().text())
