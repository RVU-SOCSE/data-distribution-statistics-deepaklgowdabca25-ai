import pandas as pd

# -------------------------------
# Load the CSV file
# -------------------------------
df = pd.read_csv(r'C:/python deepak/prog7.csv')

print("Dataset:")
print(df)

# -------------------------------
# Select correct column
# -------------------------------
col = 'Growth_rate_percent'   # change if needed

# -------------------------------
# Statistical summary
# -------------------------------
description = df.describe()

# -------------------------------
# Quantiles
# -------------------------------
quantiles = df[col].quantile([0.25, 0.5, 0.75])

# -------------------------------
# Skewness and Kurtosis
# -------------------------------
skewness = df[col].skew()
kurtosis = df[col].kurt()

# -------------------------------
# Value counts
# -------------------------------
value_counts = df[col].value_counts()

# -------------------------------
# Output
# -------------------------------
print("\nStatistical Summary:\n", description)

print("\nQuantiles:\n", quantiles)

print("\nSkewness:", skewness)

print("Kurtosis:", kurtosis)

print("\nValue Counts:\n", value_counts)
