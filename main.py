from fastapi import FastAPI, UploadFile, File
from random import randint
from pydantic import BaseModel
from typing import List
# import ml_model


app = FastAPI()


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


@app.post("/recognize_ingredients", response_model=RecognizeIngredientsResponse)
async def recognize_ingredients(image: UploadFile = File(...)):
    # Save the uploaded image temporarily
    with open("temp_image.jpg", "wb") as temp_image:
        temp_image.write(await image.read())

    # Pass the image to the machine learning model for ingredient recognition
    # recognized_ingredients = ml_model.recognize_ingredients("temp_image.jpg")
    recognized_ingredients = [f"ing{i}" for i in range(randint(2, 20))]

    # Return the list of recognized ingredients
    return {"ingredients": recognized_ingredients}


@app.post("/suggest_menus", response_model=SuggestMenusResponse)
async def suggest_menus(request: SuggestMenusRequest):
    ingredients = request.ingredients

    # Pass the ingredients to the machine learning model for menu suggestions
    # suggested_menus = ml_model.suggest_menus(ingredients)
    suggested_menus = [
        {
            "name": f"menu{i}",
            "description": f"Ini deskripsi untuk menu {i}. Menu ini memiliki ciri khas tersendiri dibanding menu-menu lain. Menu yang satu ini juga jadi favorit karena prosesnya mudah untuk dilakukan",
            "image_url": "https://picsum.photos/400/300",
            "ingredients": [f"ing{i}_{j}" for j in range(randint(4, 20))],
            "steps": [
                f"This is step {j} in making menu{i}. You have to follow this religiously no matter what. Please follow the instructions clearly or else you will suffer."
                for j in range(randint(5, 15))
            ],
        } for i in range(randint(0, 10))
    ]

    # Return the list of suggested menus
    return {"menus": suggested_menus}
