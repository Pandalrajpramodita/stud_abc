from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
df = joblib.load("model/score_train_model.pkl")

# Define input data schema using Pydantic
class StuData(BaseModel):
    study_time: float
    attendance: float
    gender_Male: int

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def root_data():
    return {"message": "Hello welcome back to the channel"}

# Prediction endpoint
@app.post("/predict")
def scr_prd(data: StuData):
    input_data = np.array([[data.study_time, data.attendance, data.gender_Male]])
    prediction = df.predict(input_data)
    return {"Predicted_score": int(prediction[0])}
