import models.ml.regressor as reg
from fastapi import FastAPI, Request, Form
from joblib import load
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import RedirectResponse


app = FastAPI(title="ML API", description="API for vehicle dataset ml model", version="1.0")
templates = Jinja2Templates(directory="templates/")
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


@app.on_event('startup')
async def load_model():
    reg.model = load('models/ml/vehicle_dt_v1.joblib')


@app.get("/", status_code=200)
def root(request: Request):
    return templates.TemplateResponse('predict.html', context={'request': request})


@app.post('/pred')
async def get_pred(request: Request):
    data = await request.form()
    Make = data['Make']
    Model = data['Model']
    Year = data['Year']
    Engine_Fuel_Type = data['Engine_Fuel_Type']
    Engine_HP = data['Engine_HP']
    Engine_Cylinders = data['Engine_Cylinders']
    Transmission_Type = data['Transmission_Type']
    Driven_Wheels = data['Driven_Wheels']
    Number_of_Doors = data['Number_of_Doors']
    Market_Category = data['Market_Category']
    Vehicle_Size = data['Vehicle_Size']
    Vehicle_Style = data['Vehicle_Style']
    highway_MPG = data['highway_MPG']
    city_mpg = data['city_mpg']
    Popularity = data['Popularity']
    to_pred = [Make, Model, Year, Engine_Fuel_Type, Engine_HP, Engine_Cylinders, Transmission_Type, Driven_Wheels,
               Number_of_Doors, Market_Category, Vehicle_Size, Vehicle_Style, highway_MPG, city_mpg, Popularity]
    pred = str(int(reg.model.predict(to_pred).tolist())) + "$"

    return templates.TemplateResponse('predict.html', context={'request': request, 'pred': pred})


