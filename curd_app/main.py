# This is where the API is defined, exposing endpoints for the end users
# Denotes the entry point of the API server
# Defines the FastAPI app and all associated routes
    # create_all(bind=engine):
# Creates DB tables based on your models if they don’t exist
    # get_db():
# Dependency to provide a DB session to routes

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schema, curd
from database import SessionLocal, engine, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependency with DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#end points
#create an employee
@app.post("/employees/", response_model=schema.EmployeeOut)
def create_employee(employee: schema.EmployeeCreate, db: Session = Depends(get_db)):
    return curd.create_employee(db=db, employee=employee)

#get all employees
@app.get("/employees/", response_model=List[schema.EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return curd.get_employees(db)

#get employee by id
@app.get("/employees/{employee_id}", response_model=schema.EmployeeOut)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = curd.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#update employee
@app.put("/employees/{employee_id}", response_model=schema.EmployeeOut)
def update_employee(employee_id: int, employee: schema.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = curd.update_employee(db=db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#delete employee
@app.delete("/employees/{employee_id}", response_model=schema.EmployeeOut)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = curd.delete_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee



