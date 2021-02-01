from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

search_recipes = [
{
        "id": 246428,
        "title": "Chicken Pot Pie",
        "image": "https://spoonacular.com/recipeImages/246428-312x231.jpg",
        "imageType": "jpg",
        "usedIngredientCount": 8,
        "missedIngredientCount": 6,
        "missedIngredients": [
            {
                "id": 10114106,
                "amount": 0.25,
                "unit": "cup",
                "unitLong": "cups",
                "unitShort": "cup",
                "aisle": "Alcoholic Beverages",
                "name": "dry sherry",
                "original": "1/4 cup dry sherry",
                "originalString": "1/4 cup dry sherry",
                "originalName": "dry sherry",
                "metaInformation": [
                    "dry"
                ],
                "meta": [
                    "dry"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/dry-sherry.png"
            },
            {
                "id": 11297,
                "amount": 2.0,
                "unit": "Tbsp",
                "unitLong": "Tbsps",
                "unitShort": "Tbsp",
                "aisle": "Produce;Spices and Seasonings",
                "name": "fresh parsley",
                "original": "2 Tbsp minced fresh parsley",
                "originalString": "2 Tbsp minced fresh parsley",
                "originalName": "minced fresh parsley",
                "metaInformation": [
                    "fresh",
                    "minced"
                ],
                "meta": [
                    "fresh",
                    "minced"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/parsley.jpg"
            },
            {
                "id": 2049,
                "amount": 1.0,
                "unit": "teaspoon",
                "unitLong": "teaspoon",
                "unitShort": "tsp",
                "aisle": "Produce;Spices and Seasonings",
                "name": "fresh thyme leaves",
                "original": "1 teaspoon chopped fresh thyme leaves",
                "originalString": "1 teaspoon chopped fresh thyme leaves",
                "originalName": "chopped fresh thyme leaves",
                "metaInformation": [
                    "fresh",
                    "chopped"
                ],
                "meta": [
                    "fresh",
                    "chopped"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/thyme.jpg"
            },
            {
                "id": 11304,
                "amount": 0.75,
                "unit": "cup",
                "unitLong": "cups",
                "unitShort": "cup",
                "aisle": "Produce",
                "name": "green peas",
                "original": "3/4 cup green peas, frozen or fresh",
                "originalString": "3/4 cup green peas, frozen or fresh",
                "originalName": "green peas, frozen or fresh",
                "metaInformation": [
                    "fresh",
                    "green"
                ],
                "meta": [
                    "fresh",
                    "green"
                ],
                "extendedName": "fresh green peas",
                "image": "https://spoonacular.com/cdn/ingredients_100x100/peas.jpg"
            },
            {
                "id": 1145,
                "amount": 6.0,
                "unit": "Tbsp",
                "unitLong": "Tbsps",
                "unitShort": "Tbsp",
                "aisle": "Milk, Eggs, Other Dairy",
                "name": "unsalted butter",
                "original": "6 Tbsp unsalted butter",
                "originalString": "6 Tbsp unsalted butter",
                "originalName": "unsalted butter",
                "metaInformation": [
                    "unsalted"
                ],
                "meta": [
                    "unsalted"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
            },
            {
                "id": 4615,
                "amount": 0.25,
                "unit": "cup",
                "unitLong": "cups",
                "unitShort": "cup",
                "aisle": "Oil, Vinegar, Salad Dressing;Baking",
                "name": "vegetable shortening",
                "original": "1/4 cup vegetable shortening, chilled",
                "originalString": "1/4 cup vegetable shortening, chilled",
                "originalName": "vegetable shortening, chilled",
                "metaInformation": [
                    "chilled"
                ],
                "meta": [
                    "chilled"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/shortening.jpg"
            }
        ],
        "usedIngredients": [
            {
                "id": 11124,
                "amount": 1.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Produce",
                "name": "carrot",
                "original": "1 carrot",
                "originalString": "1 carrot",
                "originalName": "carrot",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"
            },
            {
                "id": 11124,
                "amount": 3.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Produce",
                "name": "carrots",
                "original": "3 carrots, thinly sliced on the diagonal",
                "originalString": "3 carrots, thinly sliced on the diagonal",
                "originalName": "carrots, thinly sliced on the diagonal",
                "metaInformation": [
                    "thinly sliced"
                ],
                "meta": [
                    "thinly sliced"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"
            },
            {
                "id": 10111143,
                "amount": 1.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Produce",
                "name": "celery stalk",
                "original": "1 celery stalk",
                "originalString": "1 celery stalk",
                "originalName": "celery stalk",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/celery.jpg"
            },
            {
                "id": 10111143,
                "amount": 3.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Produce",
                "name": "celery stalks",
                "original": "3 celery stalks, thinly sliced on the diagonal",
                "originalString": "3 celery stalks, thinly sliced on the diagonal",
                "originalName": "celery stalks, thinly sliced on the diagonal",
                "metaInformation": [
                    "thinly sliced"
                ],
                "meta": [
                    "thinly sliced"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/celery.jpg"
            },
            {
                "id": 5006,
                "amount": 3.5,
                "unit": "pound",
                "unitLong": "pounds",
                "unitShort": "lb",
                "aisle": "Meat",
                "name": "chicken",
                "original": "1 (3 1/2 pound) frying chicken",
                "originalString": "1 (3 1/2 pound) frying chicken",
                "originalName": "frying chicken",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg"
            },
            {
                "id": 1123,
                "amount": 1.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Milk, Eggs, Other Dairy",
                "name": "egg",
                "original": "1 egg whisked with 1 Tbsp water",
                "originalString": "1 egg whisked with 1 Tbsp water",
                "originalName": "egg whisked with 1 Tbsp water",
                "metaInformation": [
                    "with 1 tbsp water"
                ],
                "meta": [
                    "with 1 tbsp water"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/egg.png"
            },
            {
                "id": 1077,
                "amount": 1.5,
                "unit": "cups",
                "unitLong": "cups",
                "unitShort": "cup",
                "aisle": "Milk, Eggs, Other Dairy",
                "name": "milk",
                "original": "1 1/2 cups milk",
                "originalString": "1 1/2 cups milk",
                "originalName": "milk",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/milk.png"
            },
            {
                "id": 11282,
                "amount": 1.25,
                "unit": "cups",
                "unitLong": "cups",
                "unitShort": "cup",
                "aisle": "Produce",
                "name": "onion",
                "original": "1 large onion, diced (about 1 1/4 cups)",
                "originalString": "1 large onion, diced (about 1 1/4 cups)",
                "originalName": "large onion, diced (about",
                "metaInformation": [
                    "diced"
                ],
                "meta": [
                    "diced"
                ],
                "extendedName": "diced onion",
                "image": "https://spoonacular.com/cdn/ingredients_100x100/brown-onion.png"
            }
        ],
        "unusedIngredients": [
            {
                "id": 15152,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Seafood",
                "name": "shrimp",
                "original": "shrimp",
                "originalString": "shrimp",
                "originalName": "shrimp",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/shrimp.png"
            },
            {
                "id": 11143,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "celery",
                "original": "celery",
                "originalString": "celery",
                "originalName": "celery",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/celery.jpg"
            },
            {
                "id": 11529,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "tomato",
                "original": "tomato",
                "originalString": "tomato",
                "originalName": "tomato",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/tomato.png"
            },
            {
                "id": 9003,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "apples",
                "original": "apples",
                "originalString": "apples",
                "originalName": "apples",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/apple.jpg"
            },
            {
                "id": 10011457,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "spinach",
                "original": "spinach",
                "originalString": "spinach",
                "originalName": "spinach",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/spinach.jpg"
            }
        ],
        "likes": 2383
    },
    {
        "id": 74351,
        "title": "Chicken With Herbed Dumplings",
        "image": "https://spoonacular.com/recipeImages/74351-312x231.jpg",
        "imageType": "jpg",
        "usedIngredientCount": 7,
        "missedIngredientCount": 7,
        "missedIngredients": [
            {
                "id": 2004,
                "amount": 1.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Produce;Spices and Seasonings",
                "name": "bay leaf",
                "original": "1 bay leaf",
                "originalString": "1 bay leaf",
                "originalName": "bay leaf",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/bay-leaves.jpg"
            },
            {
                "id": 10211821,
                "amount": 4.0,
                "unit": "servings",
                "unitLong": "servings",
                "unitShort": "servings",
                "aisle": "Produce",
                "name": "bell pepper",
                "original": "freshly ground black pepper",
                "originalString": "freshly ground black pepper",
                "originalName": "freshly ground black pepper",
                "metaInformation": [
                    "black",
                    "freshly ground"
                ],
                "meta": [
                    "black",
                    "freshly ground"
                ],
                "extendedName": "black bell pepper",
                "image": "https://spoonacular.com/cdn/ingredients_100x100/bell-pepper-orange.png"
            },
            {
                "id": 1001,
                "amount": 3.0,
                "unit": "Tbsps",
                "unitLong": "Tbsps",
                "unitShort": "Tbsp",
                "aisle": "Milk, Eggs, Other Dairy",
                "name": "butter",
                "original": "3 Tbsps butter",
                "originalString": "3 Tbsps butter",
                "originalName": "butter",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
            },
            {
                "id": 11156,
                "amount": 1.0,
                "unit": "Tbsp",
                "unitLong": "Tbsp",
                "unitShort": "Tbsp",
                "aisle": "Produce",
                "name": "chives",
                "original": "1 Tbsp minced chives",
                "originalString": "1 Tbsp minced chives",
                "originalName": "minced chives",
                "metaInformation": [
                    "minced"
                ],
                "meta": [
                    "minced"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/fresh-chives.jpg"
            },
            {
                "id": 9150,
                "amount": 1.0,
                "unit": "tablespoon",
                "unitLong": "tablespoon",
                "unitShort": "Tbsp",
                "aisle": "Produce",
                "name": "lemon",
                "original": "a tablespoon of lemon to taste",
                "originalString": "a tablespoon of lemon to taste",
                "originalName": "a of lemon to taste",
                "metaInformation": [
                    "to taste"
                ],
                "meta": [
                    "to taste"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/lemon.png"
            },
            {
                "id": 2041,
                "amount": 1.0,
                "unit": "Tbsp",
                "unitLong": "Tbsp",
                "unitShort": "Tbsp",
                "aisle": "Produce",
                "name": "tarragon",
                "original": "1 Tbsp minced tarragon",
                "originalString": "1 Tbsp minced tarragon",
                "originalName": "minced tarragon",
                "metaInformation": [
                    "minced"
                ],
                "meta": [
                    "minced"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/tarragon.jpg"
            },
            {
                "id": 11887,
                "amount": 1.0,
                "unit": "Tbsp",
                "unitLong": "Tbsp",
                "unitShort": "Tbsp",
                "aisle": "Pasta and Rice",
                "name": "tomato paste",
                "original": "1 Tbsp tomato paste (optional)",
                "originalString": "1 Tbsp tomato paste (optional)",
                "originalName": "tomato paste (optional)",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/tomato-paste.jpg"
            }
        ],
        "usedIngredients": [
            {
                "id": 11124,
                "amount": 2.0,
                "unit": "large",
                "unitLong": "larges",
                "unitShort": "large",
                "aisle": "Produce",
                "name": "carrots",
                "original": "2 carrots large dice",
                "originalString": "2 carrots large dice",
                "originalName": "carrots large dice",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"
            },
            {
                "id": 11143,
                "amount": 2.0,
                "unit": "ribs",
                "unitLong": "ribs",
                "unitShort": "ribs",
                "aisle": "Produce",
                "name": "celery",
                "original": "2 ribs celery large dice",
                "originalString": "2 ribs celery large dice",
                "originalName": "celery large dice",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/celery.jpg"
            },
            {
                "id": 5006,
                "amount": 1.0,
                "unit": "qts",
                "unitLong": "quart",
                "unitShort": "qts",
                "aisle": "Meat",
                "name": "chicken",
                "original": "1 qtstock from one chicken carcass (add water if you don't have a quart)",
                "originalString": "1 qtstock from one chicken carcass (add water if you don't have a quart)",
                "originalName": "tock from one chicken carcass (add water if you don't have a quart)",
                "metaInformation": [
                    "(add water if you don't have a quart)"
                ],
                "meta": [
                    "(add water if you don't have a quart)"
                ],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg"
            },
            {
                "id": 5006,
                "amount": 2.0,
                "unit": "cups",
                "unitLong": "cups",
                "unitShort": "cup",
                "aisle": "Meat",
                "name": "chicken",
                "original": "2 cups cooked chicken (or 20 ozs boneless chicken thighs, see post for instructions)",
                "originalString": "2 cups cooked chicken (or 20 ozs boneless chicken thighs, see post for instructions)",
                "originalName": "cooked chicken (or 20 ozs boneless chicken thighs, see post for instructions)",
                "metaInformation": [
                    "boneless",
                    "cooked",
                    "for instructions)"
                ],
                "meta": [
                    "boneless",
                    "cooked",
                    "for instructions)"
                ],
                "extendedName": "cooked boneless chicken",
                "image": "https://spoonacular.com/cdn/ingredients_100x100/whole-chicken.jpg"
            },
            {
                "id": 1123,
                "amount": 4.0,
                "unit": "large",
                "unitLong": "larges",
                "unitShort": "large",
                "aisle": "Milk, Eggs, Other Dairy",
                "name": "eggs",
                "original": "4 large eggs",
                "originalString": "4 large eggs",
                "originalName": "eggs",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/egg.png"
            },
            {
                "id": 1077,
                "amount": 1.0,
                "unit": "cup",
                "unitLong": "cup",
                "unitShort": "cup",
                "aisle": "Milk, Eggs, Other Dairy",
                "name": "milk",
                "original": "1 cup milk",
                "originalString": "1 cup milk",
                "originalName": "milk",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/milk.png"
            },
            {
                "id": 11282,
                "amount": 1.0,
                "unit": "",
                "unitLong": "",
                "unitShort": "",
                "aisle": "Produce",
                "name": "onion",
                "original": "1 onion, diced",
                "originalString": "1 onion, diced",
                "originalName": "onion, diced",
                "metaInformation": [
                    "diced"
                ],
                "meta": [
                    "diced"
                ],
                "extendedName": "diced onion",
                "image": "https://spoonacular.com/cdn/ingredients_100x100/brown-onion.png"
            }
        ],
        "unusedIngredients": [
            {
                "id": 15152,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Seafood",
                "name": "shrimp",
                "original": "shrimp",
                "originalString": "shrimp",
                "originalName": "shrimp",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/shrimp.png"
            },
            {
                "id": 11529,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "tomato",
                "original": "tomato",
                "originalString": "tomato",
                "originalName": "tomato",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/tomato.png"
            },
            {
                "id": 9003,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "apples",
                "original": "apples",
                "originalString": "apples",
                "originalName": "apples",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/apple.jpg"
            },
            {
                "id": 10011457,
                "amount": 1.0,
                "unit": "serving",
                "unitLong": "serving",
                "unitShort": "serving",
                "aisle": "Produce",
                "name": "spinach",
                "original": "spinach",
                "originalString": "spinach",
                "originalName": "spinach",
                "metaInformation": [],
                "meta": [],
                "image": "https://spoonacular.com/cdn/ingredients_100x100/spinach.jpg"
            }
        ],
        "likes": 2
    }
]

class RecipesSearch(Resource):
  def get(self, ingredients):
    return search_recipes

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

api.add_resource(RecipesSearch, '/search/<string:ingredients>')

if __name__ == '__main__':
    app.run(debug=True)