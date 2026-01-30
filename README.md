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
- Flask
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Docker
- HTML / CSS

---

## 🧠 Model Used

- Deep Learning Autoencoder (Unsupervised Learning)
- Statistical Thresholding (95th Percentile Method)
- Rule-Based Attack Classification

This forms a Hybrid Intrusion Detection System.

---

## 📂 Project Structure

    iot-anomaly-detection/
    │
    ├── webapp/
    │ ├── app.py
    │ ├── templates/
    │ │ └── index.html
    │ └── static/
    │ └── style.css
    │
    ├── Dockerfile
    ├── requirements.txt
    ├── .gitignore
    ├── .dockerignore
    └── README.md


---

## ✅ System Requirements

- Docker Desktop

Download from: https://www.docker.com/products/docker-desktop/

No additional software is required.

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
Upload an IoT network traffic CSV file

Click "Analyze Network"

View anomaly detection results

Supported datasets:

TON_IoT

BoT-IoT

Similar IoT traffic datasets

📊 Output Features
The system displays:

Total Records

Normal Traffic Count

Anomalies Detected

Detection Threshold

Top Suspicious Records

Attack Type Labels

Example Attacks:

Possible DDoS Attack

Possible Port Scan

Possible Data Exfiltration

Possible MITM Attack

