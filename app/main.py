import io
import zipfile

import requests
from fastapi import FastAPI
import pandas as pd


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/adresses.parquet")
async def get_addresses():
    url = "https://data.geo.admin.ch/ch.swisstopo.amtliches-gebaeudeadressverzeichnis/csv/2056/ch.swisstopo.amtliches-gebaeudeadressverzeichnis.zip"
    r = requests.get(url)
    stream = io.BytesIO(r.content)
    zip_file = zipfile.ZipFile(stream)
    zip_file.extract("pure_adr.csv", "/data")
    data = pd.read_csv("/data/pure_adr.csv", sep=";")
    return list(data.columns)
