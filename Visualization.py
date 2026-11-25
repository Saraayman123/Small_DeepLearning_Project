import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Cleaned_Customers.csv')
print(df.shape)
print("------------- Histogram -----------")
plt.hist(df['gender'], bins=3, edgecolor='white')
plt.xlabel('gender')
plt.ylabel('StreamingTv')
plt.show()

print("------------- Density Plot -----------")
sns.kdeplot(data=df, x='MonthlyCharges',fill=True)
plt.show()

print("------------- Bar Plot -----------")
counts = df['Contract'].value_counts()
counts.plot(kind='bar')
plt.ylabel('Churn')
plt.show()

print("------------- Count Plot -----------")
sns.countplot(data=df, x='gender')
plt.show()

print("------------- Box Plot -----------")
sns.boxplot(data=df,y='MonthlyCharges')
plt.show()

print("------------- Scatter Plot -----------")
sns.scatterplot(data=df, x='Age',y='MonthlyCharges')
plt.show()

print("------------- Correlation Heatmap -----------")
cols = ['MonthlyCharges', 'TotalCharges','tenure']
corr = df[cols].corr()
print(corr.round(2))
sns.heatmap(corr, annot=True,cmap='BrBG', vmin=-1, vmax=1)
plt.show()

print("------------- Pair Plot -----------")
sns.pairplot(df[['MonthlyCharges', 'TotalCharges','tenure']])
plt.show()