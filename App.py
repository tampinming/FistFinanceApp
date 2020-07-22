import pandas as pd
import streamlit as str
import mapbox as mb
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as st
import numpy as np
import time

done = False
data = []
str.title("Hello This is my first finance app")
str.write("BITCOIN Live Price")
for m in range(1,10):
    a = st.get_live_price("BTC-USD")
    data.append(a)
chart = str.line_chart(data)
while not done:
    data2 = []
    for n in range(1,10):
        b = st.get_live_price("BTC-USD")
        data2.append(b)
    chart.add_rows(data2)


