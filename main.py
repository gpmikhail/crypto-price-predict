import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model, Model, Sequential
from tensorflow.keras.layers import Dense, LSTM
from functions import *

# Symbol, Interval and Start Date setup
symbol = "BTCUSDT"
interval ='1h'
start_date = "1 Mar,2022"

# Get Data from Binance
#data = get_data(symbol, interval, start_date)

# Load Data (use after you already downloaded data from Binance)
data = load_data(symbol + '.csv')

# Draw chart from data
show_chart(data, symbol)

# Correlation with "close" column
#correlation = data.corr()
#print(correlation["close"].sort_values(ascending=False))

# Split in Train and Test
x = data[["open", "high", "low", "volume"]]
y = data["close"]
x = x.to_numpy()
y = y.to_numpy()
y = y.reshape(-1, 1)

xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=42)

# LSTM neural network setup
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape= (xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()

# Fit model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(xtrain, ytrain, batch_size=1, epochs=10)

# Save model
model.save(symbol + '_saved_model')

# Load model
#model = keras.models.load_model(symbol + '_saved_model')

# Prediction test
features = np.array([[42252.02, 42800.00, 42125.48, 17891.660470]])
print(model.predict(features))