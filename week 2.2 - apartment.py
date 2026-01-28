from typing import Union

from fastapi import FastAPI

app = FastAPI()

price_per_m2 = 5000

def evaluate_apartment(features : dict):
    surface = features.get("surface", 0)
    prediction = surface * price_per_m2
    return prediction

@app.get("/")
def read_root():
    return {"message": "Welcome to the Real Estate API!"}

@app.get("/real_estate/{surface}")
def serve_apartment_valuation(surface: int):
    features = {"surface" : surface}
    value = evaluate_apartment(features)
    return {
        "input_surface": surface,
        "predicted_price": value,
        "currency": "EUR"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

