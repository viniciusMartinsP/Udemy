from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path(
        '',
        views.RecipeListViewHome.as_view(),
        name="home"
    ),

    path(
        'recipes/search/',
        views.RecipeListViewSearch.as_view(),
        name="search"
    ),

    path(
        'recipes/tags/<slug:slug>',
        views.RecipeListViewTag.as_view(),
        name="tag"
    ),

    path(
        'recipes/category/<int:category_id>/',
        views.RecipeListViewCategory.as_view(),
        name="category"
    ),

    path(
        'recipes/<int:pk>/',
        views.RecipeDetail.as_view(),
        name="recipe"
    ),

    # API'S
    path(
        'recipes/api/v1',
        views.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1"
    ),

    path(
        'recipes/api/v1/<int:pk>/',
        views.RecipeDetailApi.as_view(),
        name="recipes_api_v1_detail",
    ),

    # TEORIA
    path(
        'recipes/pages/theorycbv.html',
        views.TheoryCBV.as_view(),
        name="theoryCBV",
    ),

    path(
        'recipes/pages/theory.html',
        views.theory,
        name="theory",
    ),
]
