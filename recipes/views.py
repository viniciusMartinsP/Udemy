import os

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import DetailView, ListView
from utils.pagination import make_pagination

from recipes.models import Recipe

PER_PAGE = int(os.environ.get('PER_PAGE', 9))


class RecipeListViewBase(ListView):
    model = Recipe
    context_object_name = 'recipes'
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published=True,
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get('recipes'),
            PER_PAGE
        )
        ctx.update(
            {'recipes': page_obj, 'pagination_range': pagination_range}
        )
        return ctx


class RecipeListViewHome(RecipeListViewBase):
    template_name = 'recipes/pages/home.html'

# def home(request):
#     recipes = Recipe.objects.filter(
#         is_published=True,
#     ).order_by('-id')

#     page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

#     messages.success(request, 'Legal ter você por aqui')

#     return render(request, 'recipes/pages/home.html', context={
#         'recipes': page_obj,
#         'pagination_range': pagination_range
#     })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category |'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


class RecipeListViewCategoy(RecipeListViewBase):
    template_name = 'recipes/pages/search.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'title': f'{ctx.get("recipes")[0].category.name} - Category - '
        })

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            category__id=self.kwargs.get('category_id')
        )


class RecipeListViewSearch(RecipeListViewBase):
    template_name = 'recipes/pages/category.html'

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get('search', '')

        if not search_term:
            raise Http404()
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term),
            ),
            is_published=True
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('search', '')
        ctx.update({
            'page_title': f'Search for {search_term}|',
            'search_term': search_term,
            'addition_url_query': f'&search={search_term}',
        })
        return ctx


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    # O Q('something')|Q(other thing) faz com que o django procure por um ou
    # outro o __contains pesquisa como se fosse %algumacoisa%.. já o
    # __icontains pesquisa ignorando case sensitive '''

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for {search_term}|',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'addition_url_query': f'&search={search_term}',
    })


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/pages/recipe-view.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'is_detail_page': True
        })

        return ctx
