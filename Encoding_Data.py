import numpy as np
import pandas as pd
df=pd.read_csv('Cleaned_Customers.csv')

print("------------- (Binning) How To Create age groups -------------")

df["Age_Group"] = pd.cut(
df["Age"],bins=[0, 25, 40, 60, np.inf],
          labels=["Young", "Adult", "Middle_Aged", "Older"],right=True)
print(df.info())

print("------------- How To Delete Columns -------------")

print(df.shape)
df = df.drop(columns=["Churn"], errors="ignore")
df = df.drop(columns=["Partner"], errors="ignore")
print(df.shape)

print("------------- How To Encode Data -------------")

print(df.dtypes)
categorical_columns = ["gender","PaymentMethod","Age_Group","InternetService","Contract","MultipleLines"]
df_encoded = pd.get_dummies(df, columns = categorical_columns, dtype=int)
print(df_encoded.shape)

df_encoded.to_csv("Encoded_Customers.csv",index=False)