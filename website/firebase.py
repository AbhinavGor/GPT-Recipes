import firebase_admin
from firebase_admin import credentials, firestore
import uuid
cred = credentials.Certificate('./gpt-recipes-2dc15-firebase-adminsdk-fg9f3-89d6d23793')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
recipe_ref = db.collection("recipes")

def add_recipe(recipe):
    msg = recipe_ref.document(uuid.uuid4()).set(recipe)
    return msg

def get_recipes():
    recipes = recipe_ref.stream()

    res = []

    for recipe in recipes:
        res.append(recipe)

    print(res)
    return res