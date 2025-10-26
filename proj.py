import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('C:/Users/amitd/Desktop/Python Practise/NUMPY/Project/Employee_data1.csv')

# ----------------------------
# Step 1: Replace inf and -inf with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Step 2: Fill numeric NaNs with column mean
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Step 3: Replace negative Salary with mean
if 'Salary(INR)' in df.columns:
    mean_salary = df['Salary(INR)'].mean()
    df['Salary(INR)'] = np.where(df['Salary(INR)'] < 0, mean_salary, df['Salary(INR)'])

# Step 4: Replace negative Experience with mean
if 'Experience(Years)' in df.columns:
    mean_exp = df['Experience(Years)'].mean()
    df['Experience(Years)'] = np.where(df['Experience(Years)'] < 0, mean_exp, df['Experience(Years)'])

# Step 5: Drop duplicates
df.drop_duplicates(inplace=True)

# Step 6: Remove Salary outliers using 3σ rule
if 'Salary(INR)' in df.columns:
    salary_mean = df['Salary(INR)'].mean()
    salary_std = df['Salary(INR)'].std()
    lower = salary_mean - 3 * salary_std
    upper = salary_mean + 3 * salary_std
    df = df[(df['Salary(INR)'] >= lower) & (df['Salary(INR)'] <= upper)]

# ----------------------------
# Save cleaned dataset
df.to_csv('cleaned_indian_employee_data.csv', index=False)

print("Clean DataSet of Employe_data")
pd.set_option('display.max_rows', None)   # Show all rows
print(df)