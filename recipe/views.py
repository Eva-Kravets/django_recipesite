from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class RecipeAll(LoginRequiredMixin, DataMixin, ListView):
    model = Dish
    template_name = 'recipe/index.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Все рецепты")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Dish.objects.filter(is_published=True)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('about')
            except:
                form.add_error(None, 'Ошибка добавления рецепта')

    else:
        form = AddPostForm()
    return render(request, 'recipe/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление рецепта'})


class ShowPost(LoginRequiredMixin, DataMixin, DetailView):
    model = Dish
    template_name = 'recipe/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class RecipeCategory(LoginRequiredMixin, DataMixin, ListView):
    model = Dish
    template_name = 'recipe/index.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('register')
    allow_empty = False

    def get_queryset(self):
        return Dish.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'recipe/about.html', {'menu': menu, 'title': 'Выпечка и десерты'})


class Advice(LoginRequiredMixin, ListView):
    model = Advice
    template_name = 'recipe/advice.html'
    context_object_name = 'advice'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Советы'
        return context


class Instruments(LoginRequiredMixin, ListView):
    model = Instruments
    template_name = 'recipe/instruments.html'
    context_object_name = 'instruments'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Инструменты'
        return context


class Serving(LoginRequiredMixin, ListView):
    model = Serving
    template_name = 'recipe/serving.html'
    context_object_name = 'serving'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Подача'
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'recipe/register.html'
    login_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        context['menu'] = second
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('about')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'recipe/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        context['menu'] = second
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('about')


def logout_user(request):
    logout(request)
    return redirect('login')










