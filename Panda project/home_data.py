import pandas as pd

home_data = pd.read_csv("train.csv")

print(home_data.describe())
avg_lot_size = round(home_data["LotArea"].mean())
newest_home_age = 2022 - home_data["YearBuilt"].max()
#print("The average lot size is")
#print(avg_lot_size)

#print(home_data.columns)
y = home_data.SalePrice
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr","TotRmsAbvGrd"]
X = home_data[feature_names]
#print(X.head)

from sklearn.tree import DecisionTreeRegressor
iowa_model = DecisionTreeRegressor(random_state = 1)
iowa_model.fit(X, y)

predictions = iowa_model.predict(X)
average = predictions.mean()
print(predictions)
print(home_data.head)