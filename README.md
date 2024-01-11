# Stock Price Analysis Web App

## Introduction
This Python script, stockprice.py, powers a simple web application designed for stock market trade signal analysis. It utilizes several libraries such as yfinance, streamlit, pandas, numpy, matplotlib, and plotly to fetch and display stock data along with trade signals based on moving averages.

## Features
1. Stock Selection: Users can select from a list of stock tickers (e.g., TSLA, SOFI, NVDA, GOOGL, AAPL).
2. Data Retrieval: The script fetches historical data for the chosen stock using yfinance.
3. Moving Averages: Calculates 100-day and 200-day moving averages.
4. Trade Signals: Generates trade signals based on the moving averages.
5. Interactive Web Interface: Utilizes streamlit for a user-friendly web interface.

## Technology Used
The stock price analysis web application is built with several key Python libraries:

1. yfinance: Fetches historical market data from Yahoo Finance.
2. streamlit: Creates the interactive web interface.
3. pandas: Handles and processes stock data.
4. numpy: Provides support for numerical computations.
5. matplotlib & plotly: Used for data visualization and interactive charts.
6. mpld3: Enhances matplotlib charts with interactive features.

## How it Works
1. Select a Stock: On the application's homepage, select a stock ticker from the dropdown menu.
2. View Data and Signals: The app displays the stock's closing price, volume, and trade signals based on the moving averages.
3. Interact with Charts: Interactive charts allow for a detailed analysis of the stock performance over time.

