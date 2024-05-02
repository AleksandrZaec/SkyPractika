from django.urls import path
from dogsapp.views import index, categories, category_dogs
from dogsapp.apps import DogsappConfig


app_name = DogsappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/',  categories, name='categories'),
    path('<int:pk>/dogs/',  category_dogs, name='category_dogs'),
]