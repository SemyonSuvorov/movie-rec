from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ratings import views as ratings_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("profile/", include("users.urls")),
    path("movies/", include("movies.urls")),
    path("rate/movie/", ratings_views.rate_movie_view, name="rate_movie"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
