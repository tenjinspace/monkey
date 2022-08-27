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
st.dataframe(df)
