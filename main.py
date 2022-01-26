from typing import Optional

from fastapi import FastAPI, File, UploadFile
# import predicting
# import models, schemas


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post("/result")
# def predict(file: UploadFile = File(...)):

#     # new_post = models.Post(**post.dict())
#     post =  predicting.predictFuntion(image_url = file)

#     return {"Predict result": post}