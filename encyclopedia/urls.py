from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entries, name="name"),
    path("search/", views.search, name="search"),
    path('create/', views.create_entry, name='create'),

]