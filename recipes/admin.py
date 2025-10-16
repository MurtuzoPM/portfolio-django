from django.contrib import admin
from .models import Recipe, Ingredient, Tag, Rating

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',) }
    search_fields = ('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    readonly_fields = ('created_at',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('tags',)
    search_fields = ('title', 'description', 'ingredients_text')
    prepopulated_fields = { 'slug': ('title',) }
    filter_horizontal = ('tags', 'ingredients')
    inlines = [RatingInline]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'score', 'created_at')
    list_filter = ('score',)
