from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from .models import Rating


def rate_movie_view(request):
    if not request.htmx:
        return HttpResponse("Not Allowed", status=400)
    object_id = request.POST.get("object_id")
    rating_value = request.POST.get("rating_value")
    user = request.user
    message = "You must a <a href='/accounts/login'>login</a> to rate this"
    if user.is_authenticated:
        message = "<span class='bg-danger py-1 px-3 text-light rounded'>An error occured.</div>"
        ctype = ContentType.objects.get(app_label='movies', model='movie')
        rating_obj = Rating.objects.create(content_type=ctype, object_id=object_id, value=rating_value, user=user)
        if rating_obj.content_object:
            message = "<span class='bg-success py-1 px-3 text-light rounded'>Rating Saved!</div>"
    return HttpResponse(message, status=200)
