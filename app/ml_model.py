import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

delay_model = joblib.load(os.path.join(BASE_DIR, "model/delay_model.pkl"))
cost_model = joblib.load(os.path.join(BASE_DIR, "model/cost_model.pkl"))
