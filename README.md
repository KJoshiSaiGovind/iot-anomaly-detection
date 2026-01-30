# IoT Network Anomaly Detection System

## 📌 Project Overview

This project implements a Deep Learning–based Intrusion Detection System (IDS) for IoT networks.

It uses an Autoencoder Neural Network to learn normal network behavior and detect anomalous traffic patterns that may indicate cyber attacks such as:

- DDoS Attacks
- Port Scanning
- Data Exfiltration
- Man-in-the-Middle (MITM) Attacks

The system is deployed as a web application using Flask and containerized using Docker for portability and easy deployment.

---

## ⚙️ Technologies Used

- Python 3
- Flask (Web Framework)
- TensorFlow / Keras (Deep Learning)
- Scikit-learn (Preprocessing)
- Pandas & NumPy (Data Handling)
- Docker (Containerization)
- HTML / CSS (Frontend)

---

## 🧠 Model Used

- Deep Learning Autoencoder (Unsupervised Learning)
- Statistical Thresholding (95th Percentile)
- Rule-Based Attack Classification

This forms a Hybrid Intrusion Detection System.

---

## 📂 Project Structure

iot-anomaly-detection/
│
├── webapp/
│ ├── app.py
│ ├── templates/
│ └── static/
│
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .dockerignore
└── README.md


---

## ✅ System Requirements

Before running this project, make sure you have:

- Docker Desktop installed
  Download: https://www.docker.com/products/docker-desktop/

No Python or extra libraries are required if using Docker.

---

## 🚀 How to Run the Project (Using Docker)

### Step 1: Clone the Repository

git clone https://github.com/KJoshiSaiGovind/iot-anomaly-detection.git
cd iot-anomaly-detection
Step 2: Build Docker Image
docker build -t iot-anomaly-app .
Step 3: Run Docker Container
docker run -p 5000:5000 iot-anomaly-app
Step 4: Open in Browser
Open any browser and go to:

http://localhost:5000
Step 5: Upload Dataset
Upload an IoT network CSV dataset (TON_IoT / BoT-IoT / similar format)

Click "Analyze Network"

View anomaly detection results and attack classification

📊 Output Features
The system displays:

Total Records

Normal Traffic Count

Anomalies Detected

Detection Threshold

Top Suspicious Records

Attack Type Labels

Example Attacks Detected:

Possible DDoS Attack

Possible Port Scan

Possible Data Exfiltration

Possible MITM Attack

⚠️ Limitations
Dataset-specific training (model trains per upload)

Processing time depends on dataset size

Not optimized for large-scale production environments

Rule-based attack labeling is heuristic

🔮 Future Enhancements
Real-time packet capture integration

LSTM-based temporal modeling

Cloud deployment (AWS / Azure)

Continuous learning system

Advanced attack classification

📜 License
This project is developed for academic purposes and final year project.


