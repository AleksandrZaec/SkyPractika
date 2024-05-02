from django.shortcuts import render

from dogsapp.models import Category
from dogsapp.models import Dog


def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogsapp/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Питомник - все наши породы'
    }
    return render(request, 'dogsapp/categories.html', context)


def category_dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Dog.objects.filter(category_id=pk),
        'title': f'Собаки породы - {category_item.name}'
    }
    return render(request, 'dogsapp/dogs.html', context)