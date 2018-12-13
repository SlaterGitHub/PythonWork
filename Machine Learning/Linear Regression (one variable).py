import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

car_data =pd.read_csv("C:\Users\Ryan\Documents\External projects\Python\Machine Learning\Datasets\car_price.csv")
print(car_data.head())
print(car_data.describe())
"""plt.scatter(car_data['Year'], car_data['Price'])
plt.title("Year vs Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()"""

features = car_data.iloc[:,0:1].values
labels = car_data.iloc[:,1].values

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.2, random_state = 0)

LinReg = LinearRegression()

LinReg.fit(train_features, train_labels)

print(LinReg.coef_)

predictions = LinReg.predict(test_features)

comparison = pd.DataFrame({'Real':test_labels, 'Predictions':predictions})

print(comparison)

print('MAE: ', metrics.mean_absolute_error(test_labels, predictions))

print('MSE: ', np.sqrt(metrics.mean_squared_error(test_labels, predictions)))

print('RMSE: ', np.sqrt(metrics.mean_squared_error(test_labels, predictions)))







