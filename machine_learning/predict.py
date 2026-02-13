import joblib   
from schema import input_data
import numpy as np

saved_model= joblib.load('model.joblib')

#prediction login code'

def make_prediction(features) -> float:
    features = np.array(features).reshape(1, -1)
    prediction = saved_model.predict(features)
    return prediction[0]
