from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="main/index.html"), name="home"),
    path('register/', views.Register.as_view(), name="register"),
]
