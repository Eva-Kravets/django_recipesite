from django.db.models import Count

from .models import *

menu = [{'title': "Главная", 'url_name': 'about'},
          {'title': "Каталог рецептов", 'url_name': 'all_recipe'},
          {'title': "Советы", 'url_name': 'advice'},
          {'title': "Идеи подачи", 'url_name': 'serving'},
          {'title': "Инструменты", 'url_name': 'instruments'},
          {'title': "Добавить рецепт", 'url_name': 'add_page'},
          ]

second = [
         {'title': "Главная", 'url_name': 'about'},
         ]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate

        user_menu = menu

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
