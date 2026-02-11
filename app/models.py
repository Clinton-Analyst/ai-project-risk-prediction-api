from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .database import Base

class ProjectPrediction(Base):
    __tablename__ = "project_predictions"

    id = Column(Integer, primary_key=True, index=True)
    budget = Column(Float)
    duration = Column(Integer)
    workers = Column(Integer)
    material_delay = Column(Float)
    weather_risk = Column(Float)
    previous_delays = Column(Integer)
    delay_probability = Column(Float)
    cost_overrun_probability = Column(Float)
    overall_risk = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
