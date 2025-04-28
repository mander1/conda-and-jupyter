import pandas as pd

# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Turn it into a DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
print(df)

# Get basic information
print(df.info())

# Select the 'Name' column
print(df['Name'])

# Filter: find people older than 28
print(df[df['Age'] > 28])
