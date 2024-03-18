from django.core.management.base import BaseCommand
from users.models import User
from movie_recsys import utils as movierec_utils
from movies.models import Movie


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?",
                            default=10, type=int)
        parser.add_argument("--movies", action="store_true", default=False)
        parser.add_argument("--users", action="store_true", default=False)

    def handle(self, *args, **options):
        count = options.get("count")
        load_movies = options.get("movies")
        generate_users = options.get("users")
        if load_movies:
            Movie.objects.all().delete()
            movie_dataset = movierec_utils.load_movie_data(limit=count)
            movies_new = [Movie(**x) for x in movie_dataset]
            movies_bulk = Movie.objects.bulk_create(movies_new, ignore_conflicts=True)
            print(f"New movies: {len(movies_bulk)}")
        if generate_users:
            profiles = movierec_utils.get_fake_profiles(count=count)
            new_users = []
            for profile in profiles:
                new_users.append(User(**profile))
            users_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)
            print(f"New users created {len(users_bulk)}")
