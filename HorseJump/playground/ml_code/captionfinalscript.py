#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load and preprocess the data
rdata = pd.read_csv("datasheet_horse.csv")


# Extract input features (X) and target variable (y)
X = rdata[['Sire', 'Dam']]
y = rdata['y_actual']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to predict y value from user's input independent variables
def predict_jump_value(sire_value, dam_value):
    input_values = np.array([[sire_value, dam_value]])
    y_pred = model.predict(input_values)
    return round(y_pred[0])


sire_value = float(input("Enter Sire value: "))
dam_value = float(input("Enter Dam value: "))

predicted_jump_value = predict_jump_value(sire_value, dam_value)
print("Predicted Jump Value:", predicted_jump_value)

# Predict on the entire dataset
y_pred = model.predict(X)
y_pred = np.array(y_pred)
y_actual = np.array(y)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_actual, y_pred)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_actual, y_pred)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)

# Calculate R-squared (R2) Score
r2 = r2_score(y_actual, y_pred)

print("Mean Absolute Error (MAE):", round(mae,3))
print("Root Mean Squared Error (RMSE):", round(rmse,3))
print("R-squared (R2) Score:", round(r2,3))


# In[ ]:




