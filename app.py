from flask import Flask, jsonify, abort, request
import requests
import os
from dotenv import load_dotenv, find_dotenv
from fractions import Fraction
import math

load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
app = Flask(__name__)


@app.route('/search', methods=['GET'])
def get_recipes():
    ingredients = request.args.get('ingredients')
    payload = {
        "apiKey": API_KEY,
        "ingredients": ingredients,
        "limitLicense": True,
        "ranking": 1,
        "ignorePantry": True,
        "number": 40
    }
    r = requests.get('https://api.spoonacular.com/recipes/findByIngredients', params=payload).json()

    new_json = []

    if r != []:
        for recipe in r:
            if recipe["missedIngredientCount"] > 5:
                continue

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



@app.route('/search/<int:recipe_id>', methods=['GET'])
def get_details(recipe_id):
    recipe_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey=' + API_KEY).json()
   
    ingredients = []
    for i in recipe_response["extendedIngredients"]:
        ingredients.append(i["original"])

    instructions = []
    if recipe_response["analyzedInstructions"] != []:
        for i in recipe_response["analyzedInstructions"][0]["steps"]:
            instructions.append(i["step"])

    new_json = []
    recipe_details = {}
    recipe_details["credit"] = recipe_response["sourceName"]
    recipe_details["ingredients"] = ingredients
    recipe_details["instructions"] = instructions
    new_json.append(recipe_details)
    
    return jsonify(new_json)

if __name__ == '__main__':
    app.run(debug=True)