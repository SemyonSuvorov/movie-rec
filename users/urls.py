from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name="profile"),
    path('ratings', views.ratings_view, name="ratings"),
    path('search-film/', views.search_film, name='search-film'),
]