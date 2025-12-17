from fastapi import APIRouter
from app.database import get_db_connection
import psycopg2.extras

router = APIRouter()

@router.get("/analytics/anomalies")
def get_anomalies():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("""
        SELECT id, device_id, type, severity, timestamp, details
        FROM anomalies
        ORDER BY timestamp DESC
    """)

    return cur.fetchall()
