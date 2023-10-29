from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for ingredient, amount in DATA['omlet'].items():
        recipe[ingredient] = amount * servings

    context = {
        'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for ingredient, amount in DATA['pasta'].items():
        recipe[ingredient] = amount * servings

    context = {
        'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for ingredient, amount in DATA['buter'].items():
        recipe[ingredient] = amount * servings

    context = {
        'recipe': recipe}
    return render(request, 'calculator/index.html', context)

