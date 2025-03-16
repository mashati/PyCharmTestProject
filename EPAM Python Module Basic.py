import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm
from pydantic import BaseModel, ValidationError
import jsonschema
from jsonschema import validate

# Data Quality Example - Pandas
print("=== Data Quality Example with Pandas ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve'],
    'Age': [25, 30, 35, np.nan, 40],
    'Salary': [50000, 60000, np.nan, 70000, 80000]
}
df = pd.DataFrame(data)

# Display missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values with mean for Age and Salary without FutureWarning
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("\nData after filling missing values:\n", df)

# Data Visualization Examples
print("\n=== Data Visualization Examples ===")
# Matplotlib
plt.figure(figsize=(10, 5))
plt.hist(df['Age'], bins=5, alpha=0.7, color='blue')
plt.title('Histogram of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# Seaborn
plt.figure(figsize=(10, 5))
sns.boxplot(x='Salary', data=df)
plt.title('Boxplot of Salaries')
plt.show()

# Plotly
fig = px.scatter(df, x='Age', y='Salary', title='Age vs Salary',
                 labels={'Age': 'Age', 'Salary': 'Salary'})
fig.show()

# Data Analysis Example - Statsmodels
print("\n=== Data Analysis Example with Statsmodels ===")
X = df['Age']
y = df['Salary']
X = sm.add_constant(X)  # Add an intercept
model = sm.OLS(y, X).fit()
print("Regression Summary:\n", model.summary())

# Data Validation Example - Pydantic
print("\n=== Data Validation Example with Pydantic ===")
class User(BaseModel):
    name: str
    age: int

# Valid user
valid_user = User(name='John', age=30)
print(f"Valid User: {valid_user}")

# Invalid user
try:
    invalid_user = User(name='John', age='thirty')  # This will raise a validation error
except ValidationError as e:
    print("Validation Error:", e)

# Data Validation Example - Jsonschema
print("\n=== Data Validation Example with Jsonschema ===")
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name", "age"]
}

# Valid data
data_valid = {"name": "Alice", "age": 30}
# Invalid data
data_invalid = {"name": "Alice", "age": "thirty"}

# Validate valid data
validate(instance=data_valid, schema=schema)
print("Valid data passed validation.")

# Validate invalid data
try:
    validate(instance=data_invalid, schema=schema)
except jsonschema.exceptions.ValidationError as e:
    print("Validation Error:", e)

print("\n=== Script Execution Completed ===")
