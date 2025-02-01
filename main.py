from fastapi import FastAPI
from src.salah import Salah
from src.location import Location
import datetime
app = FastAPI()

@app.get("/")
def root():
    return {
        'name': 'Next Salah API',
    }

@app.get("/all_salah")
def get_all_salah(
        address: str = 'Cairo, Egypt',
        date: datetime.date = datetime.date.today()
    ):
    location = Location(address)
    salah = Salah(
        location.geo_coords(),
        location.timezone()
    )

    return salah.get_all_salah(date)

@app.get("/next_salah")
def get_next_salah(
        address: str = 'Cairo, Egypt'
    ):
    location = Location(address)
    salah = Salah(
        location.geo_coords(),
        location.timezone()
    )

    return salah.get_next_salah()