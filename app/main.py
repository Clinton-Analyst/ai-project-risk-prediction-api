from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import numpy as np

from .database import engine, get_db
from . import models
from .schemas import ProjectInput
from .ml_model import delay_model, cost_model

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "AI Project Risk API is running"}

@app.post("/predict")
def predict_project_risk(project: ProjectInput, db: Session = Depends(get_db)):
    
    features = np.array([[
        project.budget,
        project.duration,
        project.workers,
        project.material_delay,
        project.weather_risk,
        project.previous_delays
    ]])

    delay_prob = delay_model.predict_proba(features)[0][1]
    cost_prob = cost_model.predict_proba(features)[0][1]

    overall_score = (delay_prob + cost_prob) / 2

    if overall_score < 0.4:
        risk_level = "Low"
    elif overall_score < 0.7:
        risk_level = "Medium"
    else:
        risk_level = "High"

    db_prediction = models.ProjectPrediction(
        budget=project.budget,
        duration=project.duration,
        workers=project.workers,
        material_delay=project.material_delay,
        weather_risk=project.weather_risk,
        previous_delays=project.previous_delays,
        delay_probability=float(delay_prob),
        cost_overrun_probability=float(cost_prob),
        overall_risk=risk_level
    )

    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)

    return {
        "delay_probability": round(float(delay_prob), 2),
        "cost_overrun_probability": round(float(cost_prob), 2),
        "overall_risk": risk_level
    }
