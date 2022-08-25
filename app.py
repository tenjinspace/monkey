import streamlit as st
import requests as r
import pandas as pd
import json

baseUrl = "https://extranet.who.int/publicemergency/api/Monkeypox/CaseSummary"
rawData = r.post(baseUrl)
rawData = rawData.json()

df = pd.DataFrame(rawData["Data"])
st.table(rawData)
st.dataframe(df)
