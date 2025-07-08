import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("deployment_data.csv")

X = df[["cpu_usage", "memory_usage", "error_rate", "response_time"]]
y = df["is_risky"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model trained and saved as model.pkl")

