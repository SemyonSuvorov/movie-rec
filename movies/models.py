import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

from ratings.models import Rating


class Movie(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True, null=True,
                                    auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating)
    ratings_last_updated = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True,
                                                null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    rating_avg = models.DecimalField(decimal_places=2, max_digits=5, blank=True,
                                     null=True)

    def rating_avg_display(self):
        now = timezone.now()
        if not self.ratings_last_updated:
            return self.calculate_rating()
        if self.ratings_last_updated > now - datetime.timedelta(minutes=1):
            return self.rating_avg
        return self.calculate_rating()

    def calculate_ratings_count(self):
        return self.ratings.all().count()

    def calculate_ratings_avg(self):
        return self.ratings.all().avg()

    def calculate_rating(self, save=True):
        rating_avg = self.calculate_ratings_avg()
        rating_count = self.calculate_ratings_count()
        self.rating_count = rating_count
        self.rating_avg = rating_avg
        self.ratings_last_updated = timezone.now()
        if save:
            self.save()
        return self.rating_avg
