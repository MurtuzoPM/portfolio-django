from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe, Tag

def home(request):
    recipes = Recipe.objects.select_related().prefetch_related('tags').order_by('-created_at')[:12]
    return render(request, 'recipes/home.html', {'recipes': recipes})

def search(request):
    query = request.GET.get('q', '').strip()
    results = Recipe.objects.none()
    if query:
        results = Recipe.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(ingredients_text__icontains=query)
        ).prefetch_related('tags')
    return render(request, 'recipes/search.html', {'recipes': results, 'query': query})

def tag(request, slug):
    tag_obj = get_object_or_404(Tag, slug=slug)
    recipes = tag_obj.recipes.prefetch_related('tags')
    return render(request, 'recipes/tag.html', {'tag': tag_obj, 'recipes': recipes})

def detail(request, slug):
    recipe = get_object_or_404(Recipe.objects.prefetch_related('tags'), slug=slug)
    steps = [s.strip() for s in (recipe.steps or '').split("\n") if s.strip()]
    ingredients = [s.strip() for s in (recipe.ingredients_text or '').split("\n") if s.strip()]
    return render(request, 'recipes/detail.html', {'recipe': recipe, 'steps': steps, 'ingredients_text': ingredients})
