# Defines Pydantic models (schemas) for request validation and response formatting
# Promotes data consistency and validation against invalid inputs
    # orm_mode = True:
# Allows Pydantic to read data directly from ORM objects (SQLAlchemy models)
# Enables smooth conversion to JSON

from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr 

class EmployeeCreate(EmployeeBase):
    pass
class EmployeeUpdate(EmployeeBase):
    pass
#This class defines what employee data looks like when returned from the API, including the ID, and lets FastAPI read it directly from the database object.
# EmployeeOut
    # → This is used when sending employee data back to the user (API response)
    # EmployeeBase
# → It already has common fields (like name, email, etc.)
# → EmployeeOut just adds one more field
    # id: int
# → Includes the employee ID (from database)
    # orm_mode = True
# → Allows FastAPI to take data directly from the database object
# → No need to convert it manually
class EmployeeOut(EmployeeBase):
    id: int
    class Config:
        orm_mode = True


