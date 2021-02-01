from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

search_recipes = [
{
        "id": 246428,
        "title": "Chicken Pot Pie",
        "missedIngredients": [
            {
                "amount": 0.25,
                "unitShort": "cup",
                "name": "dry sherry",
                "original": "1/4 cup dry sherry"
            },
            {
                "amount": 2.0,
                "unitShort": "Tbsp",
                "name": "fresh parsley",
                "original": "2 Tbsp minced fresh parsley"
            },
            {
                "amount": 1.0,
                "unitShort": "tsp",
                "name": "fresh thyme leaves",
                "original": "1 teaspoon chopped fresh thyme leaves"
            },
            {
                "amount": 0.75,
                "unitShort": "cup",
                "name": "green peas",
                "original": "3/4 cup green peas, frozen or fresh"
            },
            {
                "amount": 6.0,
                "unitShort": "Tbsp",
                "name": "unsalted butter",
                "original": "6 Tbsp unsalted butter",
            },
            {
                "amount": 0.25,
                "unitShort": "cup",
                "name": "vegetable shortening",
                "original": "1/4 cup vegetable shortening, chilled"
            }
        ],
        "usedIngredients": [
            {
                "amount": 3.0,
                "unitShort": "",
                "name": "carrots",
                "original": "3 carrots, thinly sliced on the diagonal"
            },
            {
                "amount": 3.0,
                "unitShort": "",
                "name": "celery stalks",
                "original": "3 celery stalks, thinly sliced on the diagonal"
            },
            {
                "amount": 3.5,
                "unitShort": "lb",
                "name": "chicken",
                "original": "1 (3 1/2 pound) frying chicken"
            },
            {
                "amount": 1.0,
                "unitShort": "",
                "name": "egg",
                "original": "1 egg whisked with 1 Tbsp water"
            },
            {
                "amount": 1.5,
                "unitShort": "cup",
                "name": "milk",
                "original": "1 1/2 cups milk"
            },
            {
                "amount": 1.25,
                "unitShort": "cup",
                "name": "onion",
                "original": "1 large onion, diced (about 1 1/4 cups)"
            }
        ],
    },
    {
        "id": 228679,
        "title": "Four Ingredient Nutella Peanut Butter Cakes",
        "image": "https://spoonacular.com/recipeImages/228679-312x231.jpg",
        "missedIngredients": [
            {
                "amount": 0.25,
                "unitShort": "cup",
                "name": "nutella",
                "original": "1/4 cup + 1 tbsp Nutella spread",
            },
            {
                "amount": 0.25,
                "unitShort": "cup",
                "name": "peanut butter",
                "original": "1/4 cup peanut butter",
            }
        ],
        "usedIngredients": [
            {
                "amount": 1.0,
                "unitShort": "large",
                "name": "egg",
                "original": "1 large egg",
            }
        ],
    },
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