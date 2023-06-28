import firebase_admin
from firebase_admin import credentials, firestore
import uuid
cred = credentials.Certificate('website\gpt-recipes-2dc15-firebase-adminsdk-fg9f3-89d6d23793.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
recipe_ref = db.collection("recipes")

def add_recipe(item_name, ingredients, instructions):
    print(uuid.uuid4())
    msg = recipe_ref.document(str(uuid.uuid4())).set({"item_name": item_name, "ingredients": ingredients, "instructions": instructions})
    return msg

def get_firebase_recipes():
    recipes = recipe_ref.stream()

    res = []

    for recipe in recipes:
        res.append(recipe.to_dict())

    print(res)
    return res