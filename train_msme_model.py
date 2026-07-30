import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

data = pd.read_csv("Dataset/archive/KAG_energydata_complete.csv")

# ----------------------------------------------------
# Create MSME Features
# ----------------------------------------------------

msme = pd.DataFrame()

# Lighting Load
msme["Lighting_Load"] = data["lights"]

# Indoor Temperature
msme["Indoor_Temperature"] = data["T1"]

# Humidity
msme["Humidity"] = data["RH_1"]

# Outdoor Temperature
msme["Outdoor_Temperature"] = data["T_out"]

# Machines Running (Derived)
msme["Machines_Running"] = (
    data["Appliances"] / 50
).clip(1, 15)

# Working Hours (Derived)
msme["Working_Hours"] = 8

# Production Load (Derived)
msme["Production_Load"] = (
    data["Appliances"] / data["Appliances"].max()
) * 100

# Occupancy (Derived)
msme["Occupancy"] = (
    data["lights"] / data["lights"].max()
) * 100

# Target
target = data["Appliances"]

# ----------------------------------------------------
# Train Model
# ----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    msme,
    target,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------------------------------
# Save Model
# ----------------------------------------------------

model_path = os.path.join(
    os.path.dirname(__file__),
    "models",
    "energy_model.pkl"
)

joblib.dump(model, model_path)

print("✅ MSME AI Model Trained Successfully")