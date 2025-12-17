from fastapi import FastAPI
from app.api.anomalies import router as anomalies_router

app = FastAPI(title="EMSIB Analytics Component")

app.include_router(anomalies_router)
