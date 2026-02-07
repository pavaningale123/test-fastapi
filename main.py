from fastapi import FastAPI, HTTPException
from typing import List
from model_val import Employee

app = FastAPI()

employees_db: List[Employee] = []

# read all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees_db

# read employee by emp_id
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

#Add new employee
@app.post("/add_employees", response_model=Employee)
def add_employee(new_emp: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees_db.append(new_emp)
    return new_emp

#Update employee by emp_id
@app.put("/update_employees/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_emp: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="Employee not found")

#Delete employee by emp_id
@app.delete("/delete_employees/{emp_id}")
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {"detail": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
