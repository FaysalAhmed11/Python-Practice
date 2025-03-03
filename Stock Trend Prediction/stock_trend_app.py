import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Fetch Stock Data
stock_ticker = "AAPL"  # You can change this to any stock symbol (e.g., "TSLA", "GOOGL")
start_date = "2010-01-01"
end_date = "2024-01-01"

df = yf.download(stock_ticker, start=start_date, end=end_date)

# Plot Closing Price
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label="Closing Price")
plt.title(f"{stock_ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# Data Preprocessing
data = df[['Close']].values
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data)

# Function to Prepare Data for LSTM
def prepare_data(data, time_step=60):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 60
X, Y = prepare_data(scaled_data, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Split Data into Training & Testing Sets
train_size = int(len(X) * 0.8)
X_train, Y_train = X[:train_size], Y[:train_size]
X_test, Y_test = X[train_size:], Y[train_size:]

# Build LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(time_step, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")

# Train the LSTM Model
history = model.fit(X_train, Y_train, epochs=10, batch_size=32, verbose=1)

# Predict Stock Prices
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions.reshape(-1, 1))

# Visualize Actual vs Predicted Prices
plt.figure(figsize=(12,6))
plt.plot(df.index[-len(Y_test):], scaler.inverse_transform(Y_test.reshape(-1, 1)), label="Actual Price", color="blue")
plt.plot(df.index[-len(predictions):], predictions, label="Predicted Price", color="red")
plt.title(f"{stock_ticker} Stock Price Prediction")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()
