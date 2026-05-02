# 📦 HTTP Data Ingestion Pipeline

## Overview

A lightweight data ingestion pipeline built in Python that demonstrates core data engineering concepts: HTTP-based data ingestion, parallel file downloads, data validation, ZIP extraction and cleanup, and containerized execution using Docker. It simulates a real-world ingestion layer used in modern data platforms.

## ⚙️ Features

- ⚡ **Concurrent downloads** using `ThreadPoolExecutor`
- 📦 **Automated ZIP extraction**
- 🧹 **Post-processing cleanup** of archives
- 🛡️ **File validation** (ZIP integrity checks)
- 🐳 **Dockerized environment** for reproducibility
- 🔁 **Fault-tolerant design** — skips bad files and continues pipeline

---

## 📂 Project Structure
http-data-ingestion-pipeline/


├── main.py                 # Core ingestion pipeline

├── downloads/              # Raw + extracted files

├── requirements.txt        # Python dependencies

├── Dockerfile              # Container build

├── docker-compose.yml      # Multi-service setup

├── .dockerignore           # Docker exclusions

└── README.md

---

## 🚀 How It Works

### 1. Ingestion
Reads a list of dataset URLs and downloads files concurrently.

### 2. Validation
Ensures HTTP responses are valid and rejects corrupted or non-ZIP files.

### 3. Processing
Extracts ZIP files into the target directory and removes processed archives.

### 4. Output
Clean CSV datasets ready for downstream analytics.

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python main.py
```

## 🐳 Run with Docker

```bash
# Build image
docker build -t http-ingestion-pipeline .

# Run container
docker run http-ingestion-pipeline
```

## 🧪 Docker Compose (Recommended)

```bash
# Start services
docker compose up --build

# Stop services
docker compose down
```
