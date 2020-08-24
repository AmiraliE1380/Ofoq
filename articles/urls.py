from django.urls import path

from . import views

urlpatterns = [
    path('articles-list/', views.articles_list, name='articles-list'),
]