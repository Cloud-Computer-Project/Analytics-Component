# EMSIB Analytics Component

## Overview
This repository contains the Analytics Component of the Energy Management System in Intelligent Buildings (EMSIB).

## Implemented Integration
### Energy Spike Anomaly Detection
The component analyzes telemetry data to detect abnormal energy consumption patterns and stores detected anomalies for dashboards and control modules.

## Technologies
- Python
- FastAPI
- PostgreSQL

## How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
