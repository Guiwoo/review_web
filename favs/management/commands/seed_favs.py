import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
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
        seeder = Seed.seeder()
        userEx = User.objects.all()
        movieEx = Movie.objects.all()
        bookEx = Book.objects.all()
        seeder.add_entity(Fav, num, {"created_by": lambda x: random.choice(userEx)})
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            fav_modles = Fav.objects.get(pk=pk)
            for b in bookEx:
                magic_num = random.randint(0, 11)
                if magic_num % 2 == 0:
                    fav_modles.books.add(b)
            for m in movieEx:
                magic_num = random.randint(0, 11)
                if magic_num % 2 == 0:
                    fav_modles.movies.add(m)
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
