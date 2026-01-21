from typing import Union

from fastapi import FastAPI

app = FastAPI()


#@app.get("/")
#def read_root():
#    return {"test : this is an API"}


@app.get("/real_estate/{surface}")
def serve_apartment_valuation(surface: int):
    features = {"surface" : surface}
    value = evaluate_apartment(features)
    return {"value": value}

def evaluate_apartment(features):
    return 1234

