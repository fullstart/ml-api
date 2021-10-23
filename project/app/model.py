# -*- coding: utf-8 -*-
"""
Prediction Model definition and helper functions.

@author: Andrey Aksenov
"""

import joblib
import pandas as pd
from sklearn.svm import SVC
from pydantic import BaseModel

# define data structures

class HeartInfo(BaseModel):
    """
    Data class to handle input data.

    Returns
    -------
    dict
        JSON structure of parameters to make 

    """
    
    val1: str


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
    return 0.75
