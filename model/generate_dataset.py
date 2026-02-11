import pandas as pd
import numpy as np

np.random.seed(42)

n_samples = 1000

data = pd.DataFrame({
    "budget": np.random.randint(500000, 10000000, n_samples),
    "duration": np.random.randint(30, 365, n_samples),
    "workers": np.random.randint(5, 100, n_samples),
    "material_delay": np.random.uniform(0, 1, n_samples),
    "weather_risk": np.random.uniform(0, 1, n_samples),
    "previous_delays": np.random.randint(0, 5, n_samples),
})

# Create artificial logic for delay
data["delay"] = (
    (data["material_delay"] > 0.6) |
    (data["weather_risk"] > 0.7) |
    (data["previous_delays"] > 2)
).astype(int)

# Create artificial logic for cost overrun
data["cost_overrun"] = (
    (data["budget"] > 7000000) |
    (data["delay"] == 1)
).astype(int)

data.to_csv("project_data.csv", index=False)

print("Dataset generated successfully!")
