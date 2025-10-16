from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    summary = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes', blank=True)
    ingredients_text = models.TextField(blank=True)
    steps = models.TextField(help_text='One step per line')
    tags = models.ManyToManyField(Tag, related_name='recipes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('recipes:detail', args=[self.slug])

    def average_rating(self) -> float:
        agg = self.ratings.aggregate(avg=models.Avg('score'))
        return float(agg['avg'] or 0)

    def __str__(self) -> str:
        return self.title

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.recipe.title} – {self.score}"
