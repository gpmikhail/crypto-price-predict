# crypto-price-predict
Crypto price prediction with Keras and Tensorflow trained on GPU
Data is downloaded from Binance with your Api

This project uses GPU to train the model, make sure you have installed:
 - tensorflow-gpu
 - [cuda-toolkit](https://developer.nvidia.com/cuda-toolkit)
 - [CUPTI](http://docs.nvidia.com/cuda/cupti/)
 - [cuDNN SDK](https://developer.nvidia.com/cudnn)
 - [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html) (optional)

To download historical data from Binance you need to [generate an Api Key](https://www.binance.com/en/support/faq/360002502072) and put it in functions.py

# Functions description

```python
get_data(symbol, interval, start_date)
```


Download from Binance and save in a .csv file historical data with selected interval from start_date to today.


```python
load_data(file)
```

Load saved .csv file.

```python
show_chart(data, symbol)
```
Generate a candlestick chart from data.
