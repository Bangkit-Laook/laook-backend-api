import os
import random
from typing import List

import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import tensorflow as tf

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecognizeIngredientsRequest(BaseModel):
    image: UploadFile

class RecognizeIngredientsResponse(BaseModel):
    ingredients: List[str]

class SuggestMenusRequest(BaseModel):
    ingredients: List[str]

class Menu(BaseModel):
    name: str
    description: str
    image_url: str
    ingredients: List[str]
    steps: List[str]

class SuggestMenusResponse(BaseModel):
    menus: List[Menu]

# Load the machine learning model
model_path = 'path/to/your/model'  # Replace with the actual path to your TensorFlow model
model = tf.keras.models.load_model(model_path)

@app.post("/recognize_ingredients", response_model=RecognizeIngredientsResponse)
async def recognize_ingredients(image: UploadFile = File(...)):
    # Save the uploaded image temporarily
    with open("temp_image.jpg", "wb") as temp_image:
        temp_image.write(await image.read())

    # Preprocess the image and perform ingredient recognition using the machine learning model
    img_tensor = tf.keras.preprocessing.image.load_img("temp_image.jpg", target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img_tensor)
    preprocessed_img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    preprocessed_img_tensor = tf.expand_dims(preprocessed_img_array, axis=0)

    # Perform prediction on the preprocessed image tensor
    predicted_labels = model.predict(preprocessed_img_tensor)

    # Convert the predicted labels to ingredient names
    recognized_ingredients = [label.decode('utf-8') for label in predicted_labels]  # Modify this conversion based on your model's output format

    # Return the list of recognized ingredients
    return {"ingredients": recognized_ingredients}

@app.post("/suggest_menus", response_model=SuggestMenusResponse)
async def suggest_menus(request: SuggestMenusRequest):
    ingredients = request.ingredients

    # Call the machine learning model for menu suggestions
    suggested_menus = [
        {
            "name": f"Menu {i}",
            "description": f"This is menu {i}",
            "image_url": f"https://example.com/menu_{i}.jpg",
            "ingredients": random.choices(ingredients, k=random.randint(1, 10)),
            "steps": [f"Step {j}" for j in range(1, random.randint(5, 15))]
        }
        for i in range(10)
    ]

    # Return the list of suggested menus
    return {"menus": suggested_menus}
