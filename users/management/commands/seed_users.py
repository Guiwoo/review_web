from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from categories.models import Category
import random


class Command(BaseCommand):

    Avariable = "Book"

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
        seeder = Seed.seeder()
        bookEx = Category.objects.filter(kind="book")
        movieEx = Category.objects.filter(kind="movie")
        seeder.add_entity(
            User,
            num,
            {
                "is_staff": False,
                "is_superuser": False,
                "fav_book_cat": lambda x: random.choice(bookEx),
                "fav_movie_cat": lambda x: random.choice(movieEx),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
