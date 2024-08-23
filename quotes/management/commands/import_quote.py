from django.core.management.base import BaseCommand, CommandParser
import csv
from quotes.models import Quote

class Command(BaseCommand):
    """Command to add Quote"""
    help = "Add Quote to database"
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file_path',type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Quote.objects.get_or_create(
                    text=row['text'],
                    author=row['author'],
                    mood=row['mood'],
                    category=row['category']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported quotes'))