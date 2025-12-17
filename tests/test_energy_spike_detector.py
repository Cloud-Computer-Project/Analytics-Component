from app.services.energy_spike_detector import detect_energy_spikes

def test_spike_detection():
    telemetry = [
        {"timestamp": "t1", "power": 10},
        {"timestamp": "t2", "power": 11},
        {"timestamp": "t3", "power": 30}
    ] * 5

    anomalies = detect_energy_spikes("device-1", telemetry)
    assert len(anomalies) > 0
