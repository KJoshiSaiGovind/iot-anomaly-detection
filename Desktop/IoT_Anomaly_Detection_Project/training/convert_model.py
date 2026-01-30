from tensorflow.keras.models import load_model

# Load old model (ignore compile)
old_model = load_model(
    "models/autoencoder_model.h5",
    compile=False
)

print("Old model loaded")

# Save in new format
old_model.save("models/autoencoder_model.keras")

print("Model converted and saved in new format")
