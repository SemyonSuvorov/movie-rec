from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from movies.models import Movie
from suggestions.models import Suggestion


@login_required
def profile_view(request):
    context = {}
    user = request.user
    suggestion_qs = Suggestion.objects.filter(user=user, did_rate=False)
    max_movies = 10
    request.session['total-new-suggestions'] = suggestion_qs.count()
    if suggestion_qs.exists():
        movie_ids = suggestion_qs.order_by("-value").values_list('object_id', flat=True)
        qs = Movie.objects.by_id_order(movie_ids)
        context['object_list'] = qs[:max_movies]
    else:
        context['object_list'] = Movie.objects.all().order_by("?")[:max_movies]
    return render(request, "users/profile.html", context)
