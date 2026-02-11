from pydantic import BaseModel

class ProjectInput(BaseModel):
    budget: float
    duration: int
    workers: int
    material_delay: float
    weather_risk: float
    previous_delays: int
