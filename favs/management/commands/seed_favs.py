import random
from django.core.management.base import BaseCommand
from favs.models import Fav
from users.models import User
from books.models import Book
from movies.models import Movie


class Command(BaseCommand):

    Avariable = "Favs"

    help = f"This command Create {Avariable}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"How many {self.Avariable}s do you want to create?",
        )

    def handle(self, *args, **options):
        num = options.get("number")
        userEx = User.objects.all()
        movieEx = Movie.objects.all()
        bookEx = Book.objects.all()
        for user in userEx:
            fav_list = Fav.objects.create(created_by=user)
            fav_list.movies.set(random.choices(movieEx))
            fav_list.books.set(random.choices(bookEx))
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
