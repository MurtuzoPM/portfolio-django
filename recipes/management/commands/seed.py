from django.core.management.base import BaseCommand
from recipes.models import Tag, Ingredient, Recipe, Rating

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        tags = ['Quick', 'Vegan', 'Dessert', 'Italian', 'Comfort']
        for t in tags:
            Tag.objects.get_or_create(name=t)

        recipes = [
            {
                'title': 'Creamy Mushroom Pasta',
                'summary': 'Rich, earthy, and ready in 20 minutes',
                'description': 'A comforting bowl of creamy mushroom pasta.',
                'ingredients_text': 'Pasta\nMushrooms\nCream\nGarlic\nParmesan',
                'steps': 'Boil pasta\nSaute mushrooms\nStir in cream\nToss with pasta\nServe hot',
                'tags': ['Italian', 'Comfort']
            },
            {
                'title': 'Vegan Buddha Bowl',
                'summary': 'Nutritious bowl with grains, greens, and tahini',
                'description': 'Healthy and colorful bowl packed with flavor.',
                'ingredients_text': 'Quinoa\nChickpeas\nSpinach\nSweet potato\nTahini',
                'steps': 'Roast sweet potato\nCook quinoa\nAssemble bowl\nDrizzle tahini\nEnjoy',
                'tags': ['Vegan', 'Quick']
            },
            {
                'title': 'Chocolate Mug Cake',
                'summary': 'A decadent dessert in minutes',
                'description': 'Single-serve chocolate cake made in a mug.',
                'ingredients_text': 'Flour\nCocoa\nSugar\nMilk\nBaking powder',
                'steps': 'Mix ingredients\nMicrowave 90 seconds\nTop with ice cream',
                'tags': ['Dessert', 'Quick']
            },
        ]

        for data in recipes:
            r, _ = Recipe.objects.get_or_create(title=data['title'], defaults={
                'summary': data['summary'],
                'description': data['description'],
                'ingredients_text': data['ingredients_text'],
                'steps': data['steps'],
            })
            for t in data['tags']:
                r.tags.add(Tag.objects.get(name=t))
            r.save()

        self.stdout.write(self.style.SUCCESS('Seeded sample recipes'))
