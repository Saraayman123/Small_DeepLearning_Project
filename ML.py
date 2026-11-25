import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df = pd.read_csv("Cleaned_Customers.csv")

print(df.shape)
print(df[["Age", "MonthlyCharges"]].head())
#---------- Choose X and y ----------
X = df[["Age"]]
y = df["MonthlyCharges"]

#---------- Train/Test Split ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#---------- Train Linear Regression ----------
model = LinearRegression()
model.fit(X_train, y_train)

print("---------- Make Predictions ----------")
predictions = model.predict(X_test)
print(pd.DataFrame({
"Actual": y_test.values,
"Predicted": predictions}).head())

#---------- Checking Errors ----------
mae = mean_absolute_error(y_test, predictions)
print("MAE:", round(mae, 2))