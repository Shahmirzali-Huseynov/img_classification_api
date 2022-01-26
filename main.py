from typing import Optional

from fastapi import FastAPI, File, UploadFile
import predicting


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/result")
def predict(file: UploadFile = File(...)):

    post =  predicting.predictFuntion(image_url = file)

    return {"Predict result": post}