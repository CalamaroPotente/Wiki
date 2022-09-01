from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entries, name="name"),
    path("search/", views.search, name="search"),
    path('create/', views.create_entry, name='create'),
    path('wiki/edit/<str:name>', views.display_edit, name='display_edit'),
    path('edit/<str:name>', views.edit, name='edit'),
    path('random/', views.random_selector, name='random'),
]
