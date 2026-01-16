from fastapi import FastAPI
from pydantic import BaseModel
import joblib # To load your trained model
import numpy as np

app = FastAPI()

# Define what data the game will send
class GameMetrics(BaseModel):
    reaction_time_ms: float
    accuracy_rate: float
    variance: float

# Load your model (ensure you have a model.pkl file)
# model = joblib.load("model.pkl") 

@app.post("/analyze")
async def analyze_data(data: GameMetrics):
    # For now, we simulate the ML logic
    # In a real scenario, use: prediction = model.predict([[data.reaction_time_ms...]])
    
    risk_score = (data.reaction_time_ms * 0.5) + (data.variance * 0.5)
    risk_level = "Low" if risk_score < 300 else "High"
    
    return {
        "assessment": "ADHD Screening",
        "risk_level": risk_level,
        "probability": round(min(risk_score / 1000, 1.0), 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
