from django.core.management.base import BaseCommand
from people.models import Person
from django_seed import Seed


class Command(BaseCommand):

    Avariable = "People"

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
        seeder.add_entity(Person, num, {"name": lambda x: seeder.faker.name()})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{num} {self.Avariable}s are created!🌈"))
