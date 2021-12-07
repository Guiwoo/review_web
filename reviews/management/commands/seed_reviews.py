import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from books.models import Book
from movies.models import Movie
from users.models import User


class Command(BaseCommand):

    Avariable = "Reviews"

    help = f"This command Create {Avariable}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many argument you want to created",
        )

    def handle(self, *args, **options):
        num = options.get("number")
        seeder = Seed.seeder()
        userEx = User.objects.all()
        movieEx = Movie.objects.all()
        bookEx = Book.objects.all()
        seeder.add_entity(
            Review,
            num,
            {
                "created_by": random.choice(userEx),
                "movie": random.choice(movieEx),
                "book": random.choice(bookEx),
                "rating": random.randint(0, 10),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
