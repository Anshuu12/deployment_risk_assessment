# 🛠️ Mini Project: Deployment Risk Prediction and Auto-Rollback System

##  Description
A mini system that:
- Predicts the risk of needing rollback from deployment changes
- Simulates monitoring
- Triggers automatic rollback if needed

##  Project Files
- `deployment_data.csv`: Mock dataset for training
- `train_model.py`: Trains a simple Random Forest model
- `predictor_api.py`: Flask API that gives rollback risk score
- `monitor_and_rollback.py`: Calls API, simulates monitoring, triggers rollback
- `rollback.sh`: Simulated rollback shell script

##  How to Run
```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Train the ML model
python train_model.py

# Step 3: Start the Flask API
python predictor_api.py

# Step 4: In another terminal, run the monitor script
python monitor_and_rollback.py
