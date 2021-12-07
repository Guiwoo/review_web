from django.core.management.base import BaseCommand
from categories import models as category_modles


class Command(BaseCommand):

    Avariable = "Categories"

    help = f"This command Create {Avariable}"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--number", default=1, help="How many argument you want to created"
    #     )

    def handle(self, *args, **options):
        Movie_Genre = [
            "Action",
            "Comedy",
            "Drama",
            "Fantasy",
            "Horror",
            "Mystery",
            "Romance",
            "Thriller",
        ]
        Book_Genre = [
            "Action and Adventure",
            "Classics",
            "Comic Book or Graphic Novel",
            "Detective and Mystery",
            "Fantasy",
            "Historical Fiction",
            "Horror",
        ]
        num = options.get("number")
        for m in Movie_Genre:
            category_modles.Category.objects.create(name=m, kind="movie")
        for b in Book_Genre:
            category_modles.Category.objects.create(name=b, kind="book")
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
