import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Python codes (vs)\employee_dataset\Messy_Employee_dataset.csv')

print(df.head())

print("Missing values in each column")
print(df.isnull().sum())

df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df['Age'].fillna(df['Age'].median(), inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.fillna(df.mean(numeric_only=True), inplace=True)

df.drop_duplicates(inplace =True)

df['Salary'] = np.where(df['Salary'] < 0,df['Salary'].mean(),df['Salary'])


salary_mean = df['Salary'].mean()


salary_std = df['Salary'].std()


lower_bound = salary_mean - (3* salary_std)


upper_bound = salary_mean + (3*salary_std)


df = df[(df['Salary'] >=lower_bound) & (df['Salary'] <= upper_bound)]



df.to_csv('cleaned_messy_employee_data.csv' , index=False)


print("data cleaning completed saved as cleaned_messy_employee_data.csv")
