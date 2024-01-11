# Stock Price Analysis Web App

## Introduction
This Python script, stockprice.py, powers a simple web application designed for stock market trade signal analysis. It utilizes several libraries such as yfinance, streamlit, pandas, numpy, matplotlib, and plotly to fetch and display stock data along with trade signals based on moving averages.

## Features
Stock Selection: Users can select from a list of stock tickers (e.g., TSLA, SOFI, NVDA, GOOGL, AAPL).
Data Retrieval: The script fetches historical data for the chosen stock using yfinance.
Moving Averages: Calculates 100-day and 200-day moving averages.
Trade Signals: Generates trade signals based on the moving averages.
Interactive Web Interface: Utilizes streamlit for a user-friendly web interface.

## Technology Used
The stock price analysis web application is built with several key Python libraries:

yfinance: Fetches historical market data from Yahoo Finance.
streamlit: Creates the interactive web interface.
pandas: Handles and processes stock data.
numpy: Provides support for numerical computations.
matplotlib & plotly: Used for data visualization and interactive charts.
mpld3: Enhances matplotlib charts with interactive features.

## How it Works
Select a Stock: On the application's homepage, select a stock ticker from the dropdown menu.
View Data and Signals: The app displays the stock's closing price, volume, and trade signals based on the moving averages.
Interact with Charts: Interactive charts allow for a detailed analysis of the stock performance over time.

