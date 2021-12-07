from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories.models import Category
from people.models import Person
import datetime
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
        writerEx = Person.objects.filter(kind="writer")
        seeder.add_entity(
            Book,
            num,
            {
                "rating": lambda x: random.randint(0, 10),
                "year": lambda x: random.randint(1900, datetime.date.today().year),
                "category": lambda x: random.choice(bookEx),
                "writer": lambda x: random.choice(writerEx),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
