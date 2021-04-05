import streamlit as st
import quandl
import datetime
import plotly.express as px


st.title("Stock Closing Prices per Month")
Yr = st.number_input('Year:', 2000, 2020)
mth = st.number_input('Month:', 1, 12)
start = datetime.datetime(Yr, mth, 1)
end = datetime.datetime(Yr, mth+1, 1)
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), ...
# third is the start date, fourth is the end date
s = st.text_input('Ticker(example:AAPL):')
quandl.ApiConfig.api_key = 'AA3yFM8u1y_LiHZX2zE7'
data = quandl.get("WIKI/" + s, start_date=start, end_date=end)

fig = px.line(data["Adj. Close"], y='Adj. Close')

st.plotly_chart(fig)

