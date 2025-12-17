from statistics import mean
from uuid import uuid4

def detect_energy_spikes(device_id, telemetry_points):
    powers = [p["power"] for p in telemetry_points]

    if len(powers) < 10:
        return []

    avg_power = mean(powers)
    anomalies = []

    for point in telemetry_points:
        deviation = (point["power"] - avg_power) / avg_power

        if deviation > 0.4:
            severity = "high" if deviation > 0.7 else "medium"

            anomalies.append({
                "id": str(uuid4()),
                "device_id": device_id,
                "timestamp": point["timestamp"],
                "type": "energy_spike",
                "severity": severity,
                "details": {
                    "measuredPower": point["power"],
                    "averagePower": avg_power,
                    "deviationPercent": round(deviation * 100, 2)
                }
            })

    return anomalies
