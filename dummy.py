import random
from random import randint
from typing import List

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import ml_model


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

@app.get("/")
async def root():
    return {"message": "App is running"}


@app.post("/recognize_ingredients", response_model=RecognizeIngredientsResponse)
async def recognize_ingredients(image: UploadFile = File(...)):
    # Save the uploaded image temporarily
    with open("temp_image.jpg", "wb") as temp_image:
        temp_image.write(await image.read())

    # Pass the image to the machine learning model for ingredient recognition
    ingredients = [
        "Chicken",
        "Squid",
        "Fish",
        "Corn",
        "Potato",
        "Cow",
        "Tahu",
        "Egg",
        "Tempeh",
        "Shrimp",
        "Carrot"
    ]
    recognized_ingredients = random.sample(ingredients, random.randint(2, 20))
    # recognized_ingredients = [f"ing{i}" for i in range(random.randint(3, 20))]
    # Return the list of recognized ingredients
    return {"ingredients": recognized_ingredients}


@app.post("/suggest_menus", response_model=SuggestMenusResponse)
async def suggest_menus(request: SuggestMenusRequest):
    ingredients = request.ingredients

    # Pass the ingredients to the machine learning model for menu suggestions
    # suggested_menus = ml_model.suggest_menus(ingredients)
    suggested_menus = [
     {
         "name": "Fried Chicken",
         "description": "Ayam goreng is an Indonesian dish which is famous for its chicken meat which is fried until crispy and seasoned.",
         "image_url": "https://awsimages.detik.net.id/community/media/visual/2021/09/18/ilustrasi-ayam-goreng_43.jpeg?w=1200",
         "ingredients": [
             "Chicken",
             "Garlic",
             "Turmeric",
             "Candlenut",
             "Lemongrass",
             "Ginger",
             "Galangal",
             "Bay leaf",
             "Salt",
             "Pepper",
             "Cooking oil",
         ],
         "steps": [
             "Pure the garlic, turmeric, candlenut, lemon grass, ginger and galangal.",
             "Heat cooking oil in a pan.",
             "Sauté ground spices, bay leaves, salt, and pepper until fragrant.",
             "Add the chicken pieces, stir well until the chicken is coated with the spices.",
             "Fry the chicken in hot oil until browned and perfectly cooked.",
             "Remove the fried chicken and drain.",
             "Serve fried chicken with warm rice and chili sauce.",
         ],
     },
     {
         "name": "Fried Squid",
         "description": "Fried calamari is a seafood dish that is famous for its fried squid covered with crispy flour.",
         "image_url": "https://www.checkyourfood.com/content/blob/Ingredients/Squid-calamari-nutritional-information-calories.jpg",
         "ingredients": [
             "squid",
             "Flour",
             "Rice flour",
             "Cornstarch",
             "Baking powder",
             "Salt",
             "Pepper",
             "Water",
             "Cooking oil",
         ],
         "steps": [
             "Clean squid and cut into slices.",
             "Mix flour, rice flour, cornstarch, baking powder, salt, and pepper in a bowl.",
             "Add water little by little while stirring until it forms a thick dough.",
             "Heat cooking oil in a pan.",
             "Dip the squid into the flour mixture until it's evenly coated.",
             "Fry the squid in hot oil until golden yellow and crispy.",
             "Remove the fried squid and drain.",
             "Serve fried calamari with chili sauce or tomato sauce.",
         ],
     },
     {
         "name": "Pepes Ikan",
         "description": "Pepes ikan is a traditional Indonesian dish made from seasoned and steamed fish in banana leaves.",
         "image_url": "https://cdn-2.tstatic.net/kaltim/foto/bank/images/resep-pepes-ikan-cue.jpg",
         "ingredients": [
             "Fish",
             "Red onion",
             "Garlic",
             "Red chili pepper",
             "Candlenut",
             "Ginger",
             "Galangal",
             "Lime leaves",
             "Salt",
             "Sugar",
             "Lime juice",
             "Banana leaf",
             "Toothpick",
         ],
         "steps": [
             "Pure shallots, garlic, red chilies, candlenuts, ginger, and galangal.",
             "Mix the ground spices with salt, sugar, and lime juice.",
             "Smear fish with spices and let stand for a few moments.",
             "Prepare a banana leaf, put the fish on it.",
             "Wrap the fish in banana leaves and tie with toothpicks.",
             "Steamed fish in a hot steamer for 30-40 minutes.",
             "Remove the pepes fish and serve while warm.",
         ],
     },
     {
         "name": "Grilled Corn",
         "description": "Roasted corn is a dish made of sweet corn roasted with various spices and sauces.",
         "image_url": "https://www.derrickriches.com/wp-content/uploads/2022/05/Depositphotos_494027806_XL-scaled-e1654030589939.jpg",
         "ingredients": [
             "Sweet corn",
             "Margarine",
             "Sweet soy sauce",
             "Salt",
             "Pepper",
             "Garlic Powder",
             "Chili sauce",
             "Leek",
         ],
         "steps": [
             "Clean the corn and boil it in salt water until cooked.",
             "Drain the corn and coat it with margarine.",
             "Mix soy sauce, salt, pepper and garlic powder in a bowl.",
             "Roll the corn in the spice mixture until it's evenly coated.",
             "Grill corn over coals or grill until browned.",
             "When the corn is cooked, remove it and sprinkle the green onions on it.",
             "Serve grilled corn with chili sauce or tomato sauce.",
         ],
     },
     {
         "name": "Fries",
         "description": "French fries are a simple dish made of potatoes that are fried until they are crispy and tasty.",
         "image_url": "https://www.thespruceeats.com/thmb/X_JGM04VusvkuGqTVan4QmBRqjI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/how-to-make-homemade-french-fries-2215971-hero-01-02f62a016f3e4aa4b41d0c27539885c3.jpg",
         "ingredients": [
             "Potato",
             "Cooking oil",
             "Salt",
             "Pepper",
             "Garlic Powder",
             "Onion Powder",
         ],
         "steps": [
             "Peel the potatoes and cut into pieces according to taste.",
             "Heat cooking oil in a pan.",
             "Fry the potatoes in hot oil until they are browned and crispy.",
             "Remove the fries and drain.",
             "Sprinkle the fried potatoes with salt, pepper, garlic powder, and shallot powder.",
             "Stir until the spices are evenly distributed with the potatoes.",
             "Serve french fries as a snack or accompaniment to other dishes.",
         ],
     },
     {
         "name": "Soto Ayam",
         "description": "Soto ayam is a delicious chicken soup dish with savory broth and spices.",
         "image_url": "https://ik.imagekit.io/dcjlghyytp1/2020/06/yusrisalaprianti.jpg?tr=f-auto",
         "ingredients": [
             "Chicken",
             "Garlic",
             "Red onion",
             "Ginger",
             "Turmeric",
             "Lemongrass",
             "Bay leaf",
             "Lime leaves",
             "Salt",
             "Pepper",
             "Pepper Powder",
             "Sun",
             "Bean sprouts",
             "Boiled eggs",
             "Celery leaves",
         ],
         "steps": [
             "Boil the chicken in water with the addition of garlic, shallots, ginger, turmeric, lemon grass, bay leaves, lime leaves, salt, pepper, and ground pepper until the chicken is cooked and the broth is rich in flavour.",
             "Remove the chicken and drain, then shred the chicken.",
             "Boil vermicelli and bean sprouts in boiling water until cooked.",
             "Prepare a bowl, put vermicelli, bean sprouts, shredded chicken, and boiled eggs on it.",
             "Pour the hot soup into a bowl.",
             "Sprinkle chicken soup with chopped celery leaves and fried onions.",
             "Serve chicken soup with chili sauce and crackers as a complement.",
         ],
     },
     {
         "name": "Tahu Isi",
         "description": "Tofu fill is a snack made of tofu stuffed with a mixture of vegetables and seasonings, then fried until crunchy.",
         "image_url": "https://asset.kompas.com/crops/ddv9YkIO4Z91U6YHKQabG3STTD0=/0x0:698x465/750x500/data/photo/2021/03/16/6050217084fc5.jpg",
         "ingredients": [
             "Know",
             "Carrot",
             "Beans",
             "Sweet corn",
             "Leek",
             "Garlic",
             "Salt",
             "Pepper",
             "Sweet soy sauce",
             "Cooking oil",
         ],
         "steps": [
             "Smash the garlic and finely chop the green onions.",
             "Heat cooking oil in a pan.",
             "Saute garlic until fragrant.",
             "Add carrots, green beans, and sweetcorn that have been cut into small pieces.",
             "Cook vegetables until cooked.",
             "Add crushed tofu, salt, pepper, and soy sauce.",
             "Stir well until the spices are evenly distributed.",
             "Take a sheet of tofu, fill it with mixed vegetables, and seal it.",
             "Fry the stuffed tofu in hot oil until browned and crispy.",
             "Remove the contents and drain.",
             "Serve stuffed tofu with chili sauce or peanut sauce.",
         ],
     },
     {
         "name": "Egg Balado",
         "description": "Telur balado is a boiled egg dish served with spicy and savory balado spices.",
         "image_url": "https://asset.kompas.com/crops/ZAz3wC7IIS7ATFMJxieKxsrZR5w=/100x67:900x600/750x500/data/photo/2023/05/04/64533129bf231.jpg",
         "ingredients": [
             "Boiled eggs",
             "Red onion",
             "Garlic",
             "Red chili pepper",
             "Tomato",
             "Salt",
             "Sugar",
             "Cooking oil",
         ],
         "steps": [
             "Pure the shallots, garlic and red chilies.",
             "Heat cooking oil in a pan.",
             "Sauté the shallots, garlic and red chilies until fragrant.",
             "Add the sliced tomatoes, salt and sugar.",
             "Cook the Balado seasoning until the tomatoes are soft and the spices are absorbed.",
             "Add boiled eggs, stir well until the eggs are coated with spices.",
             "Remove the balado eggs and serve with warm rice.",
         ],
     },
     {
         "name": "Stir-fried Tempeh",
         "description": "Tumis tempe is a simple dish made of sliced tempeh and stir-fried with savory spices.",
         "image_url": "https://thepeskyvegan.com/wp-content/uploads/2021/01/teriyaki-tempeh-stir-fry-wok.jpg",
         "ingredients": [
             "Tempeh",
             "Red onion",
             "Garlic",
             "Red chili pepper",
             "Sweet soy sauce",
             "Salt",
             "Sugar",
             "Cooking oil",
         ],
         "steps": [
             "Cut tempe into thin slices.",
             "Heat cooking oil in a pan.",
             "Sauté the shallots, garlic and red chilies until fragrant.",
             "Add tempeh, stir well until tempe is coated with spices.",
             "Add sweet soy sauce, salt and sugar.",
             "Cook stir-fried tempeh until perfectly cooked.",
             "Remove the stir-fried tempeh and serve as a complementary dish.",
         ],
     },
     {
         "name": "Balado Shrimp",
         "description": "Udang balado is a shrimp dish served with spicy and savory balado spices.",
         "image_url": "https://1.bp.blogspot.com/-2SsQrWDx82g/Tq-oy6oHraI/AAAAAAAAAeY/jVQTsEhmwrw/s1600/Prawn+Balado+01p.jpg",
         "ingredients": [
             "Shrimp",
             "Red onion",
             "Garlic",
             "Red chili pepper",
             "Tomato",
             "Salt",
             "Sugar",
             "Cooking oil",
         ],
         "steps": [
             "Peel the prawns and clean them.",
             "Pure the shallots, garlic and red chilies.",
             "Heat cooking oil in a pan.",
             "Sauté the shallots, garlic and red chilies until fragrant.",
             "Add the sliced tomatoes, salt and sugar.",
             "Cook the Balado seasoning until the tomatoes are soft and the spices are absorbed.",
             "Add the prawns, stir well until the prawns are coated with the spices.",
             "Cook the balado prawns until the prawns are perfectly cooked.",
             "Remove the balado prawns and serve with warm rice.",
         ],
     },
     {
         "name": "Carrot Curry",
         "description": "Carrot curry is a typical Indonesian curry dish made from carrots cooked in a spiced, rich curry sauce.",
         "image_url": "https://www.indianhealthyrecipes.com/wp-content/uploads/2020/10/carrot-curry-recipe.jpg",
         "ingredients": [
             "Carrot",
             "Red onion",
             "Garlic",
             "Red chili pepper",
             "Turmeric",
             "Ginger",
             "Coconut cream",
             "Salt",
             "Sugar",
             "Cooking oil",
         ],
         "steps": [
             "Peel the carrots and cut into pieces according to taste.",
             "Pure the shallots, garlic, red chilies, turmeric, and ginger.",
             "Heat cooking oil in a pan.",
             "Saute ground spices until fragrant.",
             "Add the carrots and stir well until the carrots are coated with the spices.",
             "Pour coconut milk, salt and sugar.",
             "Cook the carrot curry over low heat until the carrots are soft and the gravy thickens.",
             "Remove the carrot curry and serve with warm rice.",
         ],
     },
]

# Randomly select a menu from the suggested_menus list
    # random_menu = random.choice(suggested_menus)

    # Return the list of suggested menus
    return {"menus": suggested_menus}