import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
df = pd.read_csv("Cleaned_Customers.csv")

#----------- Loading and Preparing Data -----------
df = df.dropna(subset=["Age", "MonthlyCharges", "tenure"])
X = df[["Age", "MonthlyCharges"]]
y = (df["tenure"] >= 60).astype(int)

#----------- Splitting the Data -----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#----------- Training a Small Neural Network -----------
model = MLPClassifier(hidden_layer_sizes=(5,),max_iter=1000, random_state=42)
model.fit(X_train, y_train)

#----------- Making Predictions & Evaluate The Model -----------
predictions = model.predict(X_test)
print("Predicted:", predictions)
print("Actual:", y_test.values)

accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions, labels=[0, 1])
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", matrix)