# -*- coding: utf-8 -*-
"""
Prediction Model definition and helper functions.

@author: Andrey Aksenov
"""

import pandas as pd
from pydantic import BaseModel, Field
import dill

# define data structures

class HeartInfo(BaseModel):
    """
    Data class to handle input data.

    Returns
    -------
    dict
        JSON structure of parameters to make 

    """

    age:      int = Field(ge=20, le=150)
    sex:      int = Field(ge=0, le=1)
    cp:       int = Field(ge=0, le=3)
    trestbps: int = Field(ge=80, le=200)
    chol:     int = Field(ge=100, le=600)
    fbs:      int = Field(ge=0, le=1)
    restecg:  int = Field(ge=0, le=2)
    thalach:  int = Field(ge=60, le=250)
    exang:    int = Field(ge=0, le=1)
    oldpeak:  float = Field(ge=0, le=7)
    slope:    int = Field(ge=0, le=2)
    ca:       int = Field(ge=0, le=4)
    thal:     int = Field(ge=0, le=3)


class HeartPredict(BaseModel):
    """
    Data class for prediction data.

    Returns
    -------
    dict
        Prediction value (0 or 1)

    """
    
    prediction: float


def predict(heart_data: HeartInfo):
    """
    Make a prediction on passed structure.

    Returns
    -------
    dict
        Prediction value (0 or 1)

    """
    with open("app/heart_model.pkl", "rb") as model_file:
        model = dill.load(model_file)
    
    data = pd.DataFrame(heart_data.dict(), index=[0]).drop(["fbs"], axis=1)
    prediction = model.predict_proba(data)
    ret_val = {"prediction": prediction[0][1]}

    return HeartPredict(**ret_val)
