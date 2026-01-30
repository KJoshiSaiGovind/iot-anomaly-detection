# Model Training Module
# IoT Anomaly Detection Project
import pandas as pd
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

# Load processed data
DATA_PATH = "data/processed/traffic_features.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Shape:", df.shape)

X = df.values

# Train-test split
X_train, X_test = train_test_split(
    X, test_size=0.2, random_state=42
)

# Autoencoder Architecture
input_dim = X_train.shape[1]

input_layer = Input(shape=(input_dim,))

# Encoder
encoded = Dense(12, activation="relu")(input_layer)
encoded = Dense(6, activation="relu")(encoded)

# Decoder
decoded = Dense(12, activation="relu")(encoded)
decoded = Dense(input_dim, activation="sigmoid")(decoded)

# Model
autoencoder = Model(inputs=input_layer, outputs=decoded)

autoencoder.compile(
    optimizer="adam",
    loss="mse"
)

autoencoder.summary()

# Early stopping
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

# Train
history = autoencoder.fit(
    X_train,
    X_train,
    epochs=30,
    batch_size=256,
    shuffle=True,
    validation_data=(X_test, X_test),
    callbacks=[early_stop]
)

# Save model
MODEL_PATH = "models/autoencoder_model.h5"
autoencoder.save(MODEL_PATH)

print("Model saved at:", MODEL_PATH)
