import pandas as pd
from binance.client import Client
import datetime as dt
import plotly.graph_objects as go

# Client Settings
api_key = 'Your Api Key'
api_secret = 'Your Secret Api'
client = Client(api_key, api_secret)

# Functions

def get_data(symbol, interval, start_date):
    klines = client.get_historical_klines(symbol, interval, start_date)
    data = pd.DataFrame(klines)
    data.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol', 'taker_quote_vol', 'ignore']
    data.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in data.close_time]
    df = data.astype(float)
    df['date'] = data.index
    df.reset_index(drop=True, inplace=True)
    df.to_csv(symbol + '.csv', index=None, header=True)
    return df

def load_data(file):
    data = pd.read_csv(file)
    #data.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in data.close_time]
    return data

def show_chart(data, symbol):
    figure = go.Figure(data=[go.Candlestick(x=data['date'],
                                            open=data["open"],
                                            high=data["high"],
                                            low=data["low"],
                                            close=data["close"])])
    figure.update_layout(title = symbol + " Price",
                     xaxis_rangeslider_visible=False)
    figure.show()