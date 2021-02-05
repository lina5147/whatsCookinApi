from flask import Flask, jsonify, abort, request
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
SECRET_KEY = os.environ.get("API_KEY")

# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)

# search_recipes = [
# {
#         "id": 246428,
#         "title": "Chicken Pot Pie",
#         "image": "https://spoonacular.com/recipeImages/641901-312x231.jpg",
#         "missedIngredients": [
#             {
#                 "amount": 0.25,
#                 "unitShort": "cup",
#                 "name": "dry sherry",
#                 "original": "1/4 cup dry sherry"
#             },
#             {
#                 "amount": 2.0,
#                 "unitShort": "Tbsp",
#                 "name": "fresh parsley",
#                 "original": "2 Tbsp minced fresh parsley"
#             },
#             {
#                 "amount": 1.0,
#                 "unitShort": "tsp",
#                 "name": "fresh thyme leaves",
#                 "original": "1 teaspoon chopped fresh thyme leaves"
#             },
#             {
#                 "amount": 0.75,
#                 "unitShort": "cup",
#                 "name": "green peas",
#                 "original": "3/4 cup green peas, frozen or fresh"
#             },
#             {
#                 "amount": 6.0,
#                 "unitShort": "Tbsp",
#                 "name": "unsalted butter",
#                 "original": "6 Tbsp unsalted butter",
#             },
#             {
#                 "amount": 0.25,
#                 "unitShort": "cup",
#                 "name": "vegetable shortening",
#                 "original": "1/4 cup vegetable shortening, chilled"
#             }
#         ],
#         "usedIngredients": [
#             {
#                 "amount": 3.0,
#                 "unitShort": "",
#                 "name": "carrots",
#                 "original": "3 carrots, thinly sliced on the diagonal"
#             },
#             {
#                 "amount": 3.0,
#                 "unitShort": "",
#                 "name": "celery stalks",
#                 "original": "3 celery stalks, thinly sliced on the diagonal"
#             },
#             {
#                 "amount": 3.5,
#                 "unitShort": "lb",
#                 "name": "chicken",
#                 "original": "1 (3 1/2 pound) frying chicken"
#             },
#             {
#                 "amount": 1.0,
#                 "unitShort": "",
#                 "name": "egg",
#                 "original": "1 egg whisked with 1 Tbsp water"
#             },
#             {
#                 "amount": 1.5,
#                 "unitShort": "cup",
#                 "name": "milk",
#                 "original": "1 1/2 cups milk"
#             },
#             {
#                 "amount": 1.25,
#                 "unitShort": "cup",
#                 "name": "onion",
#                 "original": "1 large onion, diced (about 1 1/4 cups)"
#             }
#         ],
#     },
#     {
#         "id": 228679,
#         "title": "Four Ingredient Nutella Peanut Butter Cakes",
#         "image": "https://spoonacular.com/recipeImages/228679-312x231.jpg",
#         "missedIngredients": [
#             {
#                 "amount": 0.25,
#                 "unitShort": "cup",
#                 "name": "nutella",
#                 "original": "1/4 cup + 1 tbsp Nutella spread",
#             },
#             {
#                 "amount": 0.25,
#                 "unitShort": "cup",
#                 "name": "peanut butter",
#                 "original": "1/4 cup peanut butter",
#             }
#         ],
#         "usedIngredients": [
#             {
#                 "amount": 1.0,
#                 "unitShort": "large",
#                 "name": "egg",
#                 "original": "1 large egg",
#             }
#         ],
#     },
# ]

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
    r = requests.get('https://api.spoonacular.com/recipes/findByIngredients?apiKey=' + SECRET_KEY + '&ingredients=' + ingredients).json()
    new_json = []

    for recipe in r:
        new_format = {}

        new_format["id"] = recipe["id"]
        new_format["title"] = recipe["title"]
        new_format["image"] = recipe["image"]

        missed_ingredients = []
        # ingredients = []
        # newFormat["additionalIngredients"] = []
        for ingredient in recipe["missedIngredients"]:
            missed_ingredients.append(ingredient["name"])
            # ingredients.append(ingredient["original"])

        # for ingredient in recipe["usedIngredients"]:
        #     ingredients.append(ingredient["original"])

        newFormat["additionalIngredients"] = missed_ingredients
        # newFormat["ingredients"] = ingredients
        new_json.append(newFormat)

    return jsonify(new_json)


@app.route('/search/<int:recipe_id>', methods=['GET'])
def get_details(recipe_id):
    ingredients_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json?apiKey=' + SECRET_KEY).json()
    intructions_response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey=' + SECRET_KEY).json()

    
    recipe_details = {}
    ingredients = []
    for i in ingredients_response["ingredients"]:
        ingredient = str(i["amount"]["us"]["value"]) + " " + i["amount"]["us"]["unit"] + " " + i["name"] 
        ingredients.append(ingredient)

    instructions = []
    for i in intructions_response[0]["steps"]:
        instructions.append(i["step"])


    recipe_details["ingredients"] = ingredients
    recipe_details["instructions"] = instructions
    
    return jsonify(recipe_details)

if __name__ == '__main__':
    app.run(debug=True)