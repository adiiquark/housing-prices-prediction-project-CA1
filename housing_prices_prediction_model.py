# -*- coding: utf-8 -*-
"""Housing prices prediction model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KxshX7EQ6I-FSAUlJUT3mhRRkWbhb5iF
"""

# HOUSING PRICES PREDICTION PROJECT
#CA1 INT254
#SUBMITTED BY ADITI,, REG NO. 12015588

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics 

# imported the og libraries

housing_prices_dataset = sklearn.datasets.fetch_california_housing()
print(housing_prices_dataset)
#gotta structure it better so load to pandas dataframe
housing_prices_dataframe = pd.DataFrame(housing_prices_dataset.data, columns = housing_prices_dataset.feature_names)

housing_prices_dataframe.head(3)

housing_prices_dataframe.shape #analyzing the data that i have

#the prediction which has to be made vala columnn
housing_prices_dataframe['Predicted price'] = housing_prices_dataset.target

housing_prices_dataframe.head(3) #now the predicted price column has been added

print(housing_prices_dataframe.isnull().sum()) #print bull values in the dataset

#i need the statistical evaluation of my dataset
print(housing_prices_dataframe.describe())

correlation = housing_prices_dataframe.corr()
#cuz i need correlation between the features of my dataset

#lets get a heatmap of the correlation of values
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Reds')

#splitting the data into tag and figue

X = housing_prices_dataframe.drop(['Predicted price'], axis=1)
Y = housing_prices_dataframe['Predicted price']

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

model = XGBRegressor() #model loading

model.fit(X_train, Y_train) #training the model with Xtrain (feed it)

#evaluation

training_data_prediction = model.predict(X_train)

print(training_data_prediction)

# R squared error
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Price vs Predicted Price")
plt.show()

# accuracy for prediction on test data
test_data_prediction = model.predict(X_test)

# R squared error
score_1 = metrics.r2_score(Y_test, test_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)