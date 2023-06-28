from django.shortcuts import render
from .firebase import add_recipe, get_firebase_recipes
import openai, os

openai.api_key = os.environ['OPENAI_KEY']
def get_recipes(request):
    res = get_firebase_recipes()
    return render(request, 'home.html', {'recipes': res})    

def create_recipe(request):
    if request.method == "GET":
        return render(request, 'add_recipe.html')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="give me a recipe to make lunch. I have " + request.POST['ingredients'],
        temperature=0,
        max_tokens=2000,
    )
    gen_recipe = response.choices[0].text
    item_name = gen_recipe.split("Ingredients:")[0]
    ingredients = gen_recipe.split("Ingredients:")[1].split("Instructions:")[0]
    instructions = gen_recipe.split("Instructions:")[1]
    print({'ingredients': ingredients, 'instructions': instructions, 'item_name': item_name})
    add_recipe(item_name, ingredients, instructions)
    return render(request, 'home.html', {'item_name': item_name, 'ingredients': ingredients, 'instructions': instructions})