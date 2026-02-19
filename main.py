from fastapi import FastAPI,Request,HTTPException
import uvicorn
import joblib
import os 
from model import return_model
import numpy as np

MODEL_PATH=os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "random_forest_iris.pkl")


app=FastAPI()


@app.get("/")
def health_check():
    return {"status":"healthy"}

@app.post("/predict")
async def predict(request: Request):

    # Load model once per request (we’ll optimize after)
    if not os.path.exists(MODEL_PATH):
        model = return_model()
    else:
        model = joblib.load(MODEL_PATH)

    data = await request.json()

    x_data = data.get("feature")

    if x_data is None:
        raise HTTPException(status_code=400, detail="Missing 'feature' key")

    try:
        x_array = np.array(x_data, dtype=float)
    except Exception:
        raise HTTPException(status_code=400, detail="Features must be numeric")

    if np.any(np.isnan(x_array)):
        raise HTTPException(status_code=400, detail="Features contain NaN")

    # Ensure 2D
    x_array = x_array.reshape(1, -1)

    prediction = model.predict(x_array)

    return {
        "prediction": int(prediction[0])
    }



if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)