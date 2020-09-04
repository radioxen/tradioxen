#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_reader import reader
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

data, ticker = reader(ticker="DOC.V", interval="30m")
df = data.drop(["Datetime", "Adj Close"], axis=1)

values = df.values
values = values.astype("float32")
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)

x = values[:,[0,1,2,4]]
y = values[:,3]

# specify columns to plot
groups = [0, 1, 2, 3, 4]
i = 1
# plot each column
plt.figure()
for group in groups:
	plt.subplot(len(groups), 1, i)
	plt.plot(scaled[:, group])
	plt.title(df.columns[group], y=0.5, loc='right')
	i += 1
plt.show()


x_train, x_test, y_train, y_test = train_test_split(x, y,
													test_size=0.1, shuffle=False)

x_train = x_train.reshape((x_train.shape[0], 1, x_train.shape[1]))
x_test = x_test.reshape((x_test.shape[0], 1, x_test.shape[1]))

#%%
model = Sequential()
model.add(LSTM(50, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
history = model.fit(x_train, y_train, epochs=50, batch_size=72, validation_data=(x_train, y_train), verbose=1, shuffle=False)
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()