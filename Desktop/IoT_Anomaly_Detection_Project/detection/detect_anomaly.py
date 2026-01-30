# Anomaly Detection Module
# IoT Anomaly Detection Project
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error

# Paths
MODEL_PATH = "models/autoencoder_model.keras"
DATA_PATH = "data/processed/traffic_features.csv"

# Load model
model = load_model(MODEL_PATH)

print("Model Loaded")

# Load data
df = pd.read_csv(DATA_PATH)
X = df.values

print("Data Loaded:", X.shape)

# Predict reconstruction
X_pred = model.predict(X)

# Calculate reconstruction error
mse = np.mean(np.power(X - X_pred, 2), axis=1)

# Set threshold (95th percentile)
threshold = np.percentile(mse, 95)

print("Anomaly Threshold:", threshold)

# Classify
anomalies = mse > threshold

df["reconstruction_error"] = mse
df["anomaly"] = anomalies

# Save results
OUTPUT_PATH = "data/processed/detection_results.csv"
df.to_csv(OUTPUT_PATH, index=False)

# Summary
total = len(df)
anomaly_count = anomalies.sum()
normal_count = total - anomaly_count

print("Total Records:", total)
print("Normal:", normal_count)
print("Anomalies:", anomaly_count)

print("Results saved at:", OUTPUT_PATH)
