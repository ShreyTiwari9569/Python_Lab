import pandas as pd

# Read CSV file
file_name = "data1.csv"

df = pd.read_csv(file_name)

# Display basic information
print("CSV File Inspector")
print("------------------")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())


# Filter rows
# Example: select rows where Age is greater than 20
filtered_data = df[df["Age"] > 20]

print("\nFiltered Data:")
print(filtered_data)

# Export filtered data
output_file = "filtered_data.csv"
filtered_data.to_csv(output_file, index=False)

print("\nFiltered data saved to:", output_file)