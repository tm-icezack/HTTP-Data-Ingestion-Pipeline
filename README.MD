HTTP Data Ingestion Pipeline

📌 Overview

This project is a lightweight data ingestion pipeline built in Python that demonstrates core data engineering concepts:

HTTP-based data ingestion
Parallel file downloads
Data validation
ZIP extraction and cleanup
Containerized execution using Docker

It simulates a real-world ingestion layer used in modern data platforms.

🏗️ Architecture
                 ┌────────────────────┐
                 │  HTTP Data Sources  │
                 │ (ZIP File URLs)    │
                 └─────────┬──────────┘
                           │
                           ▼
             ┌──────────────────────────┐
             │  Downloader (Python)     │
             │  - requests              │
             │  - ThreadPoolExecutor    │
             └─────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │ Local Storage (downloads/)   │
        │ - Raw ZIP files              │
        └─────────┬────────────────────┘
                  │
                  ▼
     ┌───────────────────────────────┐
     │ Validation Layer              │
     │ - File integrity checks       │
     │ - ZIP verification            │
     └─────────┬────────────────────┘
               │
               ▼
     ┌───────────────────────────────┐
     │ Unzip Processor              │
     │ - Extract CSV files          │
     │ - Remove invalid archives    │
     └─────────┬────────────────────┘
               │
               ▼
        ┌────────────────────┐
        │ Clean Data Ready   │
        │ for Analytics / DB │
        └────────────────────┘


⚙️ Features
⚡ Concurrent downloads using ThreadPoolExecutor
📦 Automated ZIP extraction
🧹 Post-processing cleanup of archives
🛡️ File validation (ZIP integrity checks)
🐳 Dockerized environment for reproducibility


📂 Project Structure
http-data-ingestion-pipeline/
│
├── main.py                 # Core ingestion pipeline
├── downloads/              # Raw + extracted files
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build
├── docker-compose.yml      # Multi-service setup
├── .dockerignore           # Docker exclusions
└── README.md


🚀 How It Works
1. Ingestion
Reads list of dataset URLs
Downloads files concurrently
2. Validation
Ensures HTTP response is valid
Rejects corrupted or non-ZIP files
3. Processing
Extracts ZIP files into target directory
Removes processed archives
4. Output
Clean CSV datasets ready for downstream analytics
▶️ Run Locally
pip install -r requirements.txt
python main.py


🐳 Run with Docker
Build image
docker build .

🧪 Docker Compose (Recommended)
docker compose up --build

Stop services:

docker compose down