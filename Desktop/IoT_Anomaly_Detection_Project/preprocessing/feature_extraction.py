# Feature Extraction Module
# IoT Anomaly Detection Project
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
DATA_PATH = "data/sample_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Original Shape:", df.shape)

# Drop non-numeric columns
df_numeric = df.select_dtypes(include=["int64", "float64"])

print("After Removing Non-Numeric:", df_numeric.shape)

# Handle missing values
df_numeric = df_numeric.fillna(df_numeric.mean())

# Normalize data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df_numeric)

# Save processed data
processed_df = pd.DataFrame(scaled_data, columns=df_numeric.columns)

OUTPUT_PATH = "data/processed/traffic_features.csv"
processed_df.to_csv(OUTPUT_PATH, index=False)

print("Processed file saved at:", OUTPUT_PATH)
