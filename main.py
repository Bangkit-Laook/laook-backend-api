from fastapi import FastAPI, UploadFile, File
from random import randint
# import ml_model


app = FastAPI()


@app.post("/recognize_ingredients")
async def recognize_ingredients(image: UploadFile = File(...)):
    # Save the uploaded image temporarily
    with open("temp_image.jpg", "wb") as temp_image:
        temp_image.write(await image.read())

    # Pass the image to the machine learning model for ingredient recognition
    # recognized_ingredients = ml_model.recognize_ingredients("temp_image.jpg")
    recognized_ingredients = [f"ing{i}" for i in range(20)]

    # Return the list of recognized ingredients
    return {"ingredients": recognized_ingredients}


@app.post("/suggest_menus")
async def suggest_menus(ingredients: list):
    print(ingredients)
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
