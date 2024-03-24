from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from movies.models import Movie
from suggestions.models import Suggestion
from ratings.models import Rating
from collections import Counter


@login_required
def profile_view(request):
    context = {}
    user = request.user
    suggestion_qs = Suggestion.objects.filter(user=user, did_rate=False)
    ratings_list = list(Rating.objects.filter(user=user, active=True).values_list('value', flat=True))
    ratings_list_count = [x[1] for x in sorted(Counter(ratings_list).items())]
    context['ratings_list_count'] = ratings_list_count
    max_movies = 10
    request.session['total-new-suggestions'] = suggestion_qs.count()
    if suggestion_qs.exists():
        movie_ids = suggestion_qs.order_by("-timestamp").values_list('object_id', flat=True)
        qs = Movie.objects.by_id_order(movie_ids)
        context['object_list'] = qs[:max_movies]
    else:
        context['object_list'] = Movie.objects.all().order_by("?")[:max_movies]
    return render(request, "users/profile.html", context)


@login_required
def ratings_view(request):
    context = {}
    user = request.user
    ratings_qs = Rating.objects.filter(user=user, active=True)
    movie_ids = ratings_qs.values_list('object_id', flat=True)
    qs = Movie.objects.by_id_order(movie_ids)
    context['object_list'] = qs
    if user.is_authenticated:
        object_list = context['object_list']
        object_ids = [x.id for x in object_list]
        my_ratings = user.rating_set.movies().as_object_dict(object_ids=object_ids)
        context['my_ratings'] = my_ratings
    return render(request, 'users/ratings.html', context)
