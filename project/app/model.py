# -*- coding: utf-8 -*-
"""
Prediction Model definition and helper functions.

@author: Andrey Aksenov
"""

import joblib
import pandas as pd
from sklearn.svm import SVC
from pydantic import BaseModel
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

    age:      int
    sex:      int
    cp:       int
    trestbps: int
    chol:     int
    fbs:      int
    restecg:  int
    thalach:  int
    exang:    int
    oldpeak:  float
    slope:    int
    ca:       int
    thal:     int


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
    prediction = model.predict(data)
    ret_val = {"prediction": prediction}

    return HeartPredict(**ret_val)
