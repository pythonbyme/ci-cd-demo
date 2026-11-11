from fastapi import FastAPI
app = FastAPI()

@app.get("/")

def home():
    return {"message": "My first CD application"}

@app.get("/salary/{monthly_salary}")

def calculate_salary(monthly_salary: int):
    annual_salary = monthly_salary * 12

    return {
        "monthly_salary" : monthly_salary,
        "annual_salary" : annual_salary
    }