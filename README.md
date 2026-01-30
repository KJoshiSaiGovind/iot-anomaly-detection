🌐 IoT Network Anomaly Detection System
📌 Project Overview
The rise of IoT devices has expanded the attack surface for cybercriminals. This project implements a Hybrid Intrusion Detection System (IDS) designed specifically for IoT environments. By leveraging Deep Learning Autoencoders, the system learns "normal" network behavior and identifies deviations as potential threats.

Key Capabilities:
Proactive Defense: Detects zero-day threats using unsupervised learning.

Attack Identification: Heuristically classifies anomalies into categories like DDoS, Port Scanning, Data Exfiltration, and MITM.

Containerized Deployment: Fully Dockerized for "plug-and-play" execution across different environments.

🧠 The Hybrid Approach
Unlike traditional signature-based systems, this project uses a two-tier detection logic:

Deep Learning Tier: An Autoencoder compresses and reconstructs input data. High reconstruction error indicates an anomaly.

Statistical Tier: Employs a 95th Percentile Thresholding strategy to dynamically separate noise from genuine threats.

Rule Tier: A heuristic engine maps detected anomalies to specific attack patterns based on network feature signatures.

⚙️ Tech Stack
Backend: Flask (Python)

AI/ML: TensorFlow, Keras, Scikit-learn

Data Science: Pandas, NumPy

DevOps: Docker

Frontend: Responsive HTML5/CSS3

📂 Project Structure
Plaintext
iot-anomaly-detection/
│
├── webapp/
│   ├── app.py              # Flask Application logic
│   ├── model_engine.py      # Deep Learning inference & logic
│   ├── templates/          # HTML files (Dashboard, Upload)
│   └── static/             # CSS & JavaScript assets
│
├── Dockerfile              # Containerization instructions
├── requirements.txt        # Python dependencies
├── .dockerignore           # Files to exclude from Docker build
└── README.md               # Project documentation
🚀 Getting Started
Prerequisites
Docker Desktop installed.

Installation & Execution
Clone the Repository

Bash
git clone https://github.com/KJoshiSaiGovind/iot-anomaly-detection.git
cd iot-anomaly-detection
Build the Image

Bash
docker build -t iot-anomaly-app .
Launch the Application

Bash
docker run -p 5000:5000 iot-anomaly-app
Access the Web UI Navigate to http://localhost:5000 in your web browser.
