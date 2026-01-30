from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import EarlyStopping


app = Flask(__name__)


def train_and_detect(df):

    # Keep numeric columns
    df_num = df.select_dtypes(include=["int64", "float64"])

    if df_num.shape[1] < 3:
        raise Exception("Not enough numeric features")

    # Fill missing values
    df_num = df_num.fillna(df_num.mean())

    # Save original for analysis
    original_df = df_num.copy()

    # Normalize
    scaler = MinMaxScaler()
    X = scaler.fit_transform(df_num)

    # Train-test split
    X_train, X_test = train_test_split(
        X, test_size=0.2, random_state=42
    )

    # Autoencoder model
    input_dim = X.shape[1]

    inp = Input(shape=(input_dim,))
    enc = Dense(12, activation="relu")(inp)
    enc = Dense(6, activation="relu")(enc)

    dec = Dense(12, activation="relu")(enc)
    out = Dense(input_dim, activation="sigmoid")(dec)

    model = Model(inp, out)
    model.compile(optimizer="adam", loss="mse")

    es = EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    )

    # Train model
    model.fit(
        X_train, X_train,
        epochs=20,
        batch_size=256,
        validation_data=(X_test, X_test),
        callbacks=[es],
        verbose=0
    )

    # Reconstruction
    X_pred = model.predict(X, batch_size=256)

    # Reconstruction error
    mse = np.mean((X - X_pred) ** 2, axis=1)

    # Threshold
    threshold = np.percentile(mse, 95)

    # Detect anomalies
    anomalies = mse > threshold

    # Extract anomaly rows
    anomaly_rows = original_df[anomalies]

    # Normal behavior reference
    normal_mean = original_df[~anomalies].mean()

    # Attack labeling
    attack_labels = []

    for i, row in anomaly_rows.iterrows():

        diff = abs(row - normal_mean)

        top_feature = diff.idxmax().lower()

        attack = "Suspicious Activity"

        if "src" in top_feature or "packet" in top_feature or "pkt" in top_feature:
            attack = "Possible DDoS Attack"

        elif "conn" in top_feature or "flow" in top_feature:
            attack = "Possible Port Scan"

        elif "dst" in top_feature or "bytes" in top_feature:
            attack = "Possible Data Exfiltration"

        elif "dur" in top_feature or "time" in top_feature:
            attack = "Possible MITM Attack"

        attack_labels.append(attack)

    # Add attack type column
    anomaly_rows["attack_type"] = attack_labels

    return (
        len(X),
        int(anomalies.sum()),
        float(threshold),
        anomaly_rows.head(10)
    )


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        file = request.files["file"]

        try:

            if not file:
                raise Exception("No file uploaded")

            df = pd.read_csv(file)

            total, anomaly, threshold, anomaly_rows = train_and_detect(df)

            result = {
                "total": total,
                "anomalies": anomaly,
                "normal": total - anomaly,
                "threshold": threshold,
                "rows": anomaly_rows.to_dict(orient="records")
            }

        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
