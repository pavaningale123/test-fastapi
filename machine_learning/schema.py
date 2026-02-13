from pydantic import BaseModel, Field,StrictFloat

class input_data(BaseModel):
    Avg_Area_Income: StrictFloat = Field(..., description="Average area income")
    Avg_Area_House_Age: StrictFloat = Field(..., description="Average area house age")
    Avg_Area_Number_of_Rooms: StrictFloat = Field(..., description="Average area number of rooms")
    Avg_Area_Number_of_Bedrooms: StrictFloat = Field(..., description="Average area number of bedrooms")
    Area_Population: StrictFloat = Field(..., description="Area population")

class output_data(BaseModel):
    Price: StrictFloat = Field(..., description="Predicted house price")
