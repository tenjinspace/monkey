import streamlit as st
import requests as r
import pandas as pd
import json
from datetime import date

today = date.today()

st.title('Moneypox data')
st.header('by WHO Health Emergency Dashboard')
st.subheader('Today is: {}'.format(today))

baseUrl = "https://extranet.who.int/publicemergency/api/Monkeypox/CaseSummary"

def getData(baseUrl):
    rawData = r.post(baseUrl)
    rawData = rawData.json()
    return rawData

def cleanData(rawData):
    df = pd.DataFrame(rawData["Data"])
    df = df.replace(r'^s*$', float('NaN'), regex = True)
    newDf = df.dropna(axis=0, subset=['ISO3'])
    return df, newDf

def displayData(newDf):
    st.dataframe(newDf)

if st.button('Click to load data'):
     rawData = getData(baseUrl)
     data = cleanData(rawData)
     displayData(data)