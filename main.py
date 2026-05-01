from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

models=joblib.load("house-model.pkl")
templates=Jinja2Templates("templates")


app=FastAPI()


@app.get("/")
async def func():
    return f"newproject"


# @app.get("/model",response_class=HTMLResponse)
# async def model(request:Request):
#     new_data=[[3,2,1500,4000,1,0,0,3]]
#     output=models.predict(new_data).item()#item gives the value only instead of the 2d array
#     return templates.TemplateResponse(request=request,name="index.html",context={"output":output})

@app.get("/predict")
async def model(request:Request):
    models=joblib.load("house-model.pkl")
    new_data=[[3,2,1500,4000,1,0,0,3]]
    output=models.predict(new_data).item()
    return {"prediction":output}