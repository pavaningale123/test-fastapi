from fastapi import FastAPI
from schema import input_data, output_data
from predict import make_prediction
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API!"}
@app.post("/predict", response_model=output_data)
def predict_price(data: input_data):
    input_features = [
        data.Avg_Area_Income,
        data.Avg_Area_House_Age,
        data.Avg_Area_Number_of_Rooms,
        data.Avg_Area_Number_of_Bedrooms,
        data.Area_Population
    ]
    predicted_price = make_prediction(input_features)
    return output_data(Price=predicted_price)
