import pandas as pd

melb_data = pd.read_csv("melb_data.csv")
filtered_melb_data = melb_data.dropna(axis=0)
#print(melb_data.columns)

#Selecting the prediction target (dependent variable)
y = filtered_melb_data.Price

#Selecting features (independent variables)
melb_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melb_data[melb_features]
#print(X.describe())
#print(X.head)

from sklearn.tree import DecisionTreeRegressor
#melb_model = DecisionTreeRegressor(random_state=1)
#melb_model.fit(X, y)

#print("Making predictions for the following 5 houses:")
#print(X.head())
#print("The predictions are")
#print(melb_model.predict(X.head()))

from sklearn.metrics import mean_absolute_error

#predicted_home_prices = melb_model.predict(X)
#print(mean_absolute_error(y, predicted_home_prices))

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
melb_model = DecisionTreeRegressor(random_state=0)
melb_model.fit(train_X, train_y)
val_predictions = melb_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))