#importing libraries

import numpy as np # used to make arrays
import pandas as pd # used to analyze dataframes(structured table - dataset)
import matplotlib.pyplot as plt # used to make plots - data visualiation library
import seaborn as sns # used to make plots - data visualiation library
from sklearn.model_selection import train_test_split # used to split data into training & testing data
from xgboost import XGBRegressor
from sklearn import metrics # used to evaluate our model , MAE

def mod(gender, age, height, weight, duration, heartrate, bodytemp):
  
  l = [gender, age, height, weight, duration, heartrate, bodytemp]

  #reading data from csv -> pandas
  calories=pd.read_csv('ml_model\calories.csv')

  exercise_data=pd.read_csv('ml_model\exercise.csv')

  #adding calories column to exercise_data comlumn wise
  calories_data = pd.concat([exercise_data,calories['Calories']], axis=1)

  #gives no. of missing values in each column
  #if there are missing values, we have to process the data to remove/replace those missing values with mean / mode/ median
  calories_data.isnull().sum()

  #convert strings to int, as regression cant read strings
  #inplace=true - used to retain the replacement
  calories_data.replace({'Gender':{'male':0, 'female':1}}, inplace=True)


  #SPLITTING INTO FEATURES & TARGET

  #X = features
  X = calories_data.drop(columns=['User_ID','Calories'], axis=1)
  
  #Y - target
  Y = calories_data['Calories']


  # SPLITTING INTO TRAIN & TEST DATA
  x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

   
  model = XGBRegressor()
  
  # training the model
  model.fit(x_train, y_train)

  # test_data_prediction = model.predict(x_test)

  # print(test_data_prediction)

  input_arr = np.asarray(l)

  #reshape the array
  input_arr_reshaped = input_arr.reshape(1,-1)

  prediction = model.predict(input_arr_reshaped)

  return str(prediction[0])

  # print(y_test)


  # mae = metrics.mean_absolute_error(y_test, test_data_prediction)


  # print("Mean Absolute Error: ", mae)


