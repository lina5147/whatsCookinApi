from flask import Flask, jsonify, abort, request
import requests
import os
from dotenv import load_dotenv, find_dotenv
from fractions import Fraction
import math

load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
app = Flask(__name__)


sample_recipes = [
    {
        "additionalIngredients": [
            "peppers"
        ],
        "id": 655620,
        "image": "https://spoonacular.com/recipeImages/655620-312x231.jpg",
        "title": "Peperonata - Bell Peppers In Tomato Sauce"
    },
    {
        "additionalIngredients": [
            "herbs"
        ],
        "id": 647572,
        "image": "https://spoonacular.com/recipeImages/647572-312x231.jpg",
        "title": "How To Make Basic Marinara Sauce"
    },
    {
        "additionalIngredients": [
            "kale"
        ],
        "id": 648729,
        "image": "https://spoonacular.com/recipeImages/648729-312x231.jpg",
        "title": "Kale With Red Onion"
    },
    {
        "additionalIngredients": [
            "parsley"
        ],
        "id": 660032,
        "image": "https://spoonacular.com/recipeImages/660032-312x231.jpg",
        "title": "Shrimps and Patatas Bravas"
    },
    {
        "additionalIngredients": [
            "chili pepper"
        ],
        "id": 660101,
        "image": "https://spoonacular.com/recipeImages/660101-312x231.jpg",
        "title": "Simple Garlic Pasta"
    },
    {
        "additionalIngredients": [
            "avocado",
            "pimenton de la vera"
        ],
        "id": 643455,
        "image": "https://spoonacular.com/recipeImages/643455-312x231.jpg",
        "title": "Fresh Cherry Tomato Salad With Red Onions, Avocado and Pimentón"
    },
    {
        "additionalIngredients": [
            "canned smoked salmon",
            "dill"
        ],
        "id": 660837,
        "image": "https://spoonacular.com/recipeImages/660837-312x231.jpg",
        "title": "Spaghetti With Smoked Salmon and Prawns"
    },
    {
        "additionalIngredients": [
            "kangkong",
            "curry paste"
        ],
        "id": 650684,
        "image": "https://spoonacular.com/recipeImages/650684-312x231.jpg",
        "title": "Malaysian Sambal Kangkong (Water Spinach)"
    },
    {
        "additionalIngredients": [
            "bread",
            "chili pepper"
        ],
        "id": 644148,
        "image": "https://spoonacular.com/recipeImages/644148-312x231.jpg",
        "title": "Gambas Al Ajo"
    },
    {
        "additionalIngredients": [
            "avocado",
            "lime"
        ],
        "id": 648439,
        "image": "https://spoonacular.com/recipeImages/648439-312x231.jpg",
        "title": "Jamie's Guacamole"
    }
]

# function to turn decimal to fraction
def fraction(num):
  fractionString = ""

  wholeNum = math.floor(num)
  if wholeNum != 0:
    fractionString += f"{wholeNum} "

  decimal = num % 1
  if decimal != 0.0:
   fractionString += f"{Fraction(num % 1).limit_denominator(8)} "
  
  return fractionString



@app.route('/search', methods=['GET'])
def get_recipes():
    ingredients = request.args.get('ingredients')
    payload = {
        "apiKey": API_KEY,
        "ingredients": ingredients,
        "limitLicense": True,
        "ranking": 2,
        "ignorePantry": True,
        "number": 20
    }
    r = requests.get('https://api.spoonacular.com/recipes/findByIngredients', params=payload).json()

    new_json = []

    if r != []:
        for recipe in r:
            new_format = {}

            new_format["id"] = recipe["id"]
            new_format["title"] = recipe["title"]
            new_format["image"] = recipe["image"]

            missed_ingredients = []
            for ingredient in recipe["missedIngredients"]:
                missed_ingredients.append(ingredient["name"])

            new_format["additionalIngredients"] = missed_ingredients

            new_json.append(new_format)

    return jsonify(new_json)
    # return jsonify(sample_recipes)


sample_details = [
    {
        "ingredients": [
            "1.0 can canned smoked salmon",
            "2.0 Tbsps fresh dill",
            "0.25 cup extra virgin olive oil",
            "1.0 Tbsp garlic",
            "10.0  prawns",
            "7.055 oz spaghetti"
        ],
        "instructions": [
            "Cook spaghetti as per packet instructions. Dish up and put in a large bowl.Use fork to loosen the smoked salmon and set aside.",
            "Heat frying pan at medium heat, add olive oil and throw in garlic and saute for a while.Then add in prawns and fry till cooked, lower heat and pour in the smoked salmon and fresh dills ~ stir fry well and off heat.Lastly pour all the ingredients on the cooked spaghetti and toss well with some pepper then serve into individual plate.Enjoy!"
        ]
    }
]


@app.route('/search/<int:recipe_id>', methods=['GET'])
def get_details(recipe_id):
    ingredients_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json?apiKey=' + API_KEY).json()
    instructions_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey=' + API_KEY).json()

    
   
    ingredients = []
    for i in ingredients_response["ingredients"]:
        measurement = fraction(i["amount"]["us"]["value"])
        ingredient = measurement + i["amount"]["us"]["unit"] + " " + i["name"]
        ingredients.append(ingredient)

    instructions = []
    if instructions_response != []:
        for i in instructions_response[0]["steps"]:
            instructions.append(i["step"])

    new_json = []
    recipe_details = {}
    recipe_details["ingredients"] = ingredients
    recipe_details["instructions"] = instructions
    new_json.append(recipe_details)
    
    # return jsonify(sample_details)
    return jsonify(new_json)

if __name__ == '__main__':
    app.run(debug=True)