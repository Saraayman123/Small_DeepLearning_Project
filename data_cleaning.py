import pandas as pd
df=pd.read_csv('Uncleaned_customers.csv')

print("To Know Number Of Columns and Rows & To Know What types of values are stored?")
print(df.shape)
print(df.info())

print("------------- To Find The Missing Values -------------")
print(df.isna().sum())

print("------------- To Handle The Missing Values -------------")

df['gender']=df['gender'].fillna('unknown')
df['Partner']=df['Partner'].fillna('unknown')
df['InternetService']=df['InternetService'].fillna('unknown')
df['Contract']=df['Contract'].fillna('unknown')
df['Churn']=df['Churn'].fillna('unknown')
df['Age']=df['Age'].fillna(df['Age'].median())
df['tenure']=df['tenure'].fillna(df['tenure'].median())
df['MonthlyCharges']=df['MonthlyCharges'].fillna(df['MonthlyCharges'].median())
df['TotalCharges']=df['TotalCharges'].fillna(df['TotalCharges'].median())
print(df.isna().sum())

print("------------- If You Want To Make Data Type Casting -------------")

df['Age']=pd.to_datetime(df['Age'],errors='coerce')
print("Before: Age Column Data Type:",df['Age'].dtype)
df['Age']=pd.to_numeric(df['Age'],errors='coerce')
print("After: Age Column Data Type:",df['Age'].dtype)

print("------------- To Solve The Problem Of Inconsistent Formatting -------------")

df['gender']=df['gender'].str.strip().str.capitalize()
df['Partner']=df['Partner'].str.strip().str.capitalize()
df['Dependents']=df['Dependents'].str.strip().str.capitalize()
df['PhoneService']=df['PhoneService'].str.strip().str.capitalize()
df['MultipleLines']=df['MultipleLines'].str.strip().str.capitalize()
df['InternetService']=df['InternetService'].str.strip().str.capitalize()
df['Contract']=df['Contract'].str.strip().str.capitalize()
df['PaymentMethod']=df['PaymentMethod'].str.strip().str.capitalize()

print("------------- How To Detect and Remove Duplicates -------------")
print(df.shape)
print(df.duplicated().sum())
clean_df = df.drop_duplicates()
print(clean_df.shape)

clean_df.to_csv("Cleaned_Customers.csv.csv",index=False)