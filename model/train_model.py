import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("project_data.csv")

X = data[[
    "budget",
    "duration",
    "workers",
    "material_delay",
    "weather_risk",
    "previous_delays"
]]

y_delay = data["delay"]
y_cost = data["cost_overrun"]

# ✅ Split ONCE for all features
X_train, X_test, y_delay_train, y_delay_test, y_cost_train, y_cost_test = train_test_split(
    X, y_delay, y_cost, 
    test_size=0.2, 
    random_state=42
)

# Train delay model
delay_model = RandomForestClassifier(random_state=42)
delay_model.fit(X_train, y_delay_train)

# Train cost model with same X_train
cost_model = RandomForestClassifier(random_state=42)
cost_model.fit(X_train, y_cost_train)

# Save models
joblib.dump(delay_model, "delay_model.pkl")
joblib.dump(cost_model, "cost_model.pkl")

print("Models trained and saved successfully!")
