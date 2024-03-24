from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name="movies"),
    path('<int:pk>/', views.movie_detail_view)
]
