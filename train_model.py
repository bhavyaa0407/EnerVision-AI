import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load Dataset
data = pd.read_csv("Dataset/archive/KAG_energydata_complete.csv")

# Features and Target
X = data.drop(columns=["Appliances", "date"])
y = data["Appliances"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model
import os

model_path = os.path.join(os.path.dirname(__file__), "models", "energy_model.pkl")
joblib.dump(model, model_path)
print("Model Trained and Saved Successfully!")