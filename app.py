from flask import Flask, jsonify, abort, request
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")

# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)

# class RecipesSearch(Resource):
#   def get(self, ingredients):
#     return search_recipes

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

# api.add_resource(RecipesSearch, '/search/<string:ingredients>')

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]
# @app.route('/todo/api/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify(tasks)

# @app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         abort(404)
#     return jsonify(task[0])


@app.route('/search', methods=['GET'])
def get_recipes():
    ingredients = request.args.get('ingredients')
    payload = {
        "apiKey": API_KEY,
        "ingredients": ingredients,
        "limitLicense": True,
        "ranking": 2,
        "ignorePantry": True
    }
    r = requests.get('https://api.spoonacular.com/recipes/findByIngredients', params=payload).json()
    new_json = []

    for recipe in r:
        # check for recipe instructions
        intructions_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe["id"]}/analyzedInstructions?apiKey=' + API_KEY).json()
        # skip recipe if it doesn't have instructions
        if intructions_response == []:
            continue

        new_format = {}

        new_format["id"] = recipe["id"]
        new_format["title"] = recipe["title"]
        new_format["image"] = recipe["image"]

        missed_ingredients = []
        for ingredient in recipe["missedIngredients"]:
            missed_ingredients.append(ingredient["name"])

        new_format["additionalIngredients"] = missed_ingredients

        # intructions_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey=' + SECRET_KEY).json()
        

        new_json.append(new_format)

    # my_list = [x for x in my_list if x.attribute == value]


    return jsonify(new_json)


@app.route('/search/<int:recipe_id>', methods=['GET'])
def get_details(recipe_id):
    ingredients_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json?apiKey=' + API_KEY).json()
    intructions_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey=' + API_KEY).json()

    
   
    ingredients = []
    for i in ingredients_response["ingredients"]:
        ingredient = str(i["amount"]["us"]["value"]) + " " + i["amount"]["us"]["unit"] + " " + i["name"] 
        ingredients.append(ingredient)

    instructions = []
    for i in intructions_response[0]["steps"]:
        instructions.append(i["step"])

    new_json = []
    recipe_details = {}
    recipe_details["ingredients"] = ingredients
    recipe_details["instructions"] = instructions
    new_json.append(recipe_details)
    
    return jsonify(new_json)

if __name__ == '__main__':
    app.run(debug=True)