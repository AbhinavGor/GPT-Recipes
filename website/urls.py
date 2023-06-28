from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_recipes, name='home'),
    path('add_recipe/', views.create_recipe, name='add_recipe')
]
