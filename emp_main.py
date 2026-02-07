from fastapi import FastAPI, HTTPException
#from emp_model import Employee
from typing import List

from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int
    department: str

app = FastAPI()

employee_db: List[Employee] = []

# read all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():
    if not employee_db:
        raise HTTPException(status_code=404, detail="No employees found")
    return employee_db
raise HTTPException(status_code=404, detail="No employees found")

# read employee by id
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# create employee
@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    employee_db.append(employee)
    return employee

# update employee
@app.put("/employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, emp in enumerate(employee_db):
        if emp.id == emp_id:
            employee_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# delete employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == emp_id:
            del employee_db[index]
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")
