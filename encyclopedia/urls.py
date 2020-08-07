from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("save", views.save, name="save"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("edited/<str:title>", views.edited, name="edited")
]
