from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int = Field(..., gt=0, description="The unique identifier for the employee")
    name: str   = Field(..., min_length=3, max_length=30, description="The name of the employee")
    department: str = Field(..., min_length=3, max_length=30, description="The department of the employee")
    age: int = Field(..., gt=0, lt=50, description="The age of the employee")