import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from streamlit.components.v1 import components
import plotly.express as px

st.write(
    """
    # Simple Stock market Trade signals
    
    ### Show the closing price and the volume and generate some trade signals
    
    """
)

#name of the ticker
ticket_symbol = st.selectbox("Select the ticker?",("TSLA","SOFI","NVDA","GOOGL","AAPL"),index=None,label_visibility="collapsed",placeholder="Please select the ticker")

if ticket_symbol!= None:
    #get the data
    ticket_data=yf.Ticker(ticket_symbol)
    tickerdf=ticket_data.history(period='1d',start='2013-12-20',end='2023-12-20')

    #generating trade signal using 100 day moving averages
    tickerdf['100-day']=tickerdf['Close'].rolling(100).mean().shift()
    tickerdf['200-day']=tickerdf['Close'].rolling(200).mean().shift()

    tickerdf['signal']=np.where(tickerdf["100-day"] > tickerdf["200-day"], 1, 0)
    tickerdf['signal']= np.where(tickerdf["100-day"] < tickerdf["200-day"], -1, tickerdf['signal'])
    tickerdf.dropna(inplace=True)

    tickerdf['return']= np.log(tickerdf['Close']).diff()
    tickerdf['system return']= tickerdf['signal']*tickerdf['return']
    tickerdf['entry']= tickerdf['signal'].diff()


    # Creating an interactive Plotly graph
    # Ensure the index is in a date format if it's a DateTimeIndex
    # Ensure that the same slice of data is used for both x and y
    # Slice the DataFrame
    plot_data = tickerdf.iloc[-1500:]

    # Creating an interactive Plotly graph using the sliced data
    fig = px.line(plot_data, x=plot_data.index.date, y=['Close', '100-day', '200-day'])

    # Rest of your plotting code...

    # Add markers for entry points
    fig.add_scatter(x=tickerdf[-1500:].loc[tickerdf.entry == 2].index, y=tickerdf[-1500:]['100-day'][tickerdf.entry == 2], mode='markers', marker=dict(color='green', size=12), name='Entry Point')
    fig.add_scatter(x=tickerdf[-1500:].loc[tickerdf.entry == -2].index, y=tickerdf[-1500:]['200-day'][tickerdf.entry == -2], mode='markers', marker=dict(color='red', size=12), name='Exit Point')
    st.write("## Trade signals")
    # Display the interactive plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)


    st.write("## Closing Prices")
    st.line_chart(tickerdf.Close)
    st.write("## Volume")
    st.bar_chart(tickerdf.Volume)