# Whats Cookin' Api

The API is hosted at https://whatscookin-api.herokuapp.com. 

## Setup

### 1. External API Configuration

- Sign up with [Spoonacular](https://spoonacular.com/food-api/console#Dashboard) to request for an API key.
- If you would like to explore the endpoints I used for What's Cookin' Api, checkout the documentation for the following:
  - [Search Recipes by Ingredients](https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients)
  - [Get Recipe Information](https://spoonacular.com/food-api/docs#Get-Recipe-Information)
  
### 2. Flask API
- Install the latest version of [Python](https://www.python.org/downloads/)
- Create a virtual environment
  1. Clone the project
  2. Python 3 comes bundled with the venv module so you can simply `cd` into the project folder and run 
  `$ python3 -m venv venv`
- Activate the environment with `$ . venv/bin/activate`
- To install all of the dependencies, run `$pip3 install -r requirements.txt
- Create a `.env` file and add the Spoonacular Api key as `API_KEY`

## Functionality

### Recipes
