import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
data = pd.read_csv("Dataset/archive/KAG_energydata_complete.csv")
x = data.drop(columns=["Appliances","date"])
y = data["Appliances"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model = RandomForestRegressor(
    n_estimators = 100,
    random_state= 42
)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

importance = model.feature_importances_
feature_importance = pd.Series(importance, index=x.columns)
feature_importance = feature_importance.sort_values(ascending = False)
print(feature_importance)

import matplotlib.pyplot as plt

feature_importance.plot(kind = "bar", figsize = (12,6))
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

new_data = [[
    30,      # lights
    19.5,    # T1
    45.0,    # RH_1
    20.0,    # T2
    44.0,    # RH_2
    19.0,    # T3
    42.0,    # RH_3
    18.5,    # T4
    40.0,    # RH_4
    19.2,    # T5
    41.0,    # RH_5
    18.8,    # T6
    43.0,    # RH_6
    19.0,    # T7
    41.0,    # RH_7
    20.0,    # T8
    40.0,    # RH_8
    18.0,    # T9
    45.0,    # RH_9
    15.0,    # T_out
    755.0,   # Press_mm_hg
    60.0,    # RH_out
    5.0,     # Windspeed
    40.0,    # Visibility
    8.0,     # Tdewpoint
    10.0,    # rv1
    12.0     # rv2
]]

prediction = model.predict(new_data)

print("Predicted Energy Consumption:", prediction[0], "Wh")