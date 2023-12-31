from fastapi import FastAPI,HTTPException
import uvicorn
app = FastAPI()


@app.get("/addition")
async def addition(num1: float, num2: float):
    result = (num1 + num2)
    return {"Addition of two number is": result}


@app.get("/subtraction")
async def subtraction(num1: float, num2: float):
    result = (num1 - num2)
    return {"Subtraction of two number is": result}


@app.get("/multiplication")
async def multiplication(num1: float, num2: float):
    result = (num1 * num2)
    return {"Multiplication of two number is": result}


@app.get("/division")
async def division(num1: float, num2: float):
    if not num2==0:
        result = (num1 / num2)
        return {"Division of two number is": result}
   raise HTTPException(status_code=404, detail="wrong division")
