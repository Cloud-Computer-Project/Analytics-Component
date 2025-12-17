CREATE TABLE anomalies (
  id UUID PRIMARY KEY,
  device_id VARCHAR(100),
  timestamp TIMESTAMP,
  type VARCHAR(50),
  severity VARCHAR(10),
  details JSONB
);
