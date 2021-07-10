from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('all/', RecipeAll.as_view(), name='all_recipe'),
    path('', about, name='about'),
    path('advice/', Advice.as_view(), name='advice'),
    path('instruments/', Instruments.as_view(), name='instruments'),
    path('serving/', Serving.as_view(), name='serving'),
    path('addpage/', addpage, name='add_page'),
    path('category/<slug:cat_slug>/', RecipeCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
