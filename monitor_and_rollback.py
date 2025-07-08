import requests
import random
import time
import subprocess

def simulate_metrics():
    return {
        "cpu_usage": round(random.uniform(10, 95), 2),
        "memory_usage": round(random.uniform(20, 90), 2),
        "error_rate": round(random.uniform(0, 5), 2),
        "response_time": round(random.uniform(50, 500), 2)
    }

def monitor():
    print("📡 Starting simulated deployment monitoring...")
    for _ in range(5):
        metrics = simulate_metrics()
        print(f"\n📊 Metrics: {metrics}")

        response = requests.post("http://127.0.0.1:5000/predict-risk", json=metrics)
        result = response.json()

        print(f"🔍 Risk: {result['prediction']} | Score: {result['risk_score']}%")

        if result["prediction"] == "High":
            print("⚠️  Risky deployment detected. Triggering rollback.")
            subprocess.run(["bash", "rollback.sh"])
        else:
            print("✅ Deployment seems safe.")

        time.sleep(2)

if __name__ == "__main__":
    monitor()


