import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:/python deepak/prog7.csv')

print("Dataset:")
print(df)

# Choose correct column (example: Growth_rate_percent)
col = 'Growth_rate_percent'

# Central tendencies
mean_value = df[col].mean()
median_value = df[col].median()
mode_value = df[col].mode()[0]

# Dispersion
min_value = df[col].min()
max_value = df[col].max()
variance_value = df[col].var()
std_dev_value = df[col].std()

# Output
print("\nDescriptive Statistics:")

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
