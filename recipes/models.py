from collections import defaultdict
from datetime import date
from turtle import title
from xml.dom import ValidationErr

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.utils.text import slugify
from tag.models import Tag


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:recipe", args=(self.id,))

    def save(self, *args, **kwargs):
        if not self.slug:
            data = str(date.today())
            slug = f'{slugify(self.title)+"-"+(data)}'
            self.slug = slug
        return super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        error_messages = defaultdict(list)
        recipe_from_db = Recipe.objects.filter(
            title__iexact=self.title
        ).first()

        # VERIFICA SE A PRIMARY KEY É DIFERENTE DA QUE JÁ ESTÁ 
        # EM USO, PARA PODER PERMITIR EDIÇÕES
        if recipe_from_db:
            if recipe_from_db.pk != self.pk:
                error_messages['title'].append(
                    'Found recipes with the same title'
                )

        if error_messages:
            raise ValidationError(error_messages)
        return super().clean()
