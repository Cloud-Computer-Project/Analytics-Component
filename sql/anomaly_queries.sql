-- Insert anomaly
INSERT INTO anomalies (id, device_id, timestamp, type, severity, details)
VALUES (:id, :device_id, :timestamp, :type, :severity, :details::jsonb);
