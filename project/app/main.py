# -*- coding: utf-8 -*-
"""
API interface module for Fast API data science model app.

Provides interface and helper function for prediction module.
"""
import datetime
from fastapi import FastAPI, Depends

from app.config import get_settings, Settings
from app.model import HeartInfo, HeartPredict, predict


app = FastAPI()

# define routes

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Get basic server info.

    Returns
    -------
    dict
        Constant string "pong" with current timestamp

    """
    return {
        "ping": "pong! "
            + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "environment": settings.environment,
        "testing": settings.testing
    }


@app.post("/predict", response_model=HeartPredict, status_code=200)
async def get_prediction(payload: HeartInfo):
    """
    Make predicition using input params.

    Parameters
    ----------
    payload : HeartInfo
        Features data to make prediction on.

    Returns
    -------
    dict
        Prediction value.

    """
    prediction_val = predict(payload)
    
    return {"prediction": prediction_val}
