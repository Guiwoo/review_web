from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from categories.models import Category
from people.models import Person
from movies.models import Movie
import datetime
import random


class Command(BaseCommand):

    Avariable = "Movie"

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
        directorEx = Person.objects.filter(kind="director")
        movieEx = Category.objects.filter(kind="movie")
        castEx = Person.objects.filter(kind="actor")
        seeder.add_entity(
            Movie,
            num,
            {
                "title": lambda x: seeder.faker.company(),
                "year": lambda x: random.randint(1900, datetime.date.today().year),
                "rating": lambda x: random.randint(0, 10),
                "director": lambda x: random.choice(directorEx),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            movie_model = Movie.objects.get(pk=pk)
            for c in castEx:
                magic = random.randint(0, 11)
                if magic % 2 == 0:
                    movie_model.cast.add(c)
            for m in movieEx:
                magic = random.randint(0, 11)
                if magic % 2 == 0:
                    movie_model.category.add(m)
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
