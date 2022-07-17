import csv
import os

from django.core.management import BaseCommand

from backend.settings import BASE_DIR
from recipes.models import Ingredient

data_file = 'ingredients.csv'
model = Ingredient

class Command(BaseCommand):
    help = 'Load data from {data_file} to DB.'

    def handle(self, *args, **options):
        with open(
            os.path.join(BASE_DIR, 'data', data_file),
            encoding='utf-8'
        ) as csv_file:
            for row in csv.reader(csv_file):
                name, measurement_unit = row
                model.objects.get_or_create(
                    name=name,
                    measurement_unit=measurement_unit
                )
        print(f'  Importing data from file {data_file}... OK')
        self.stdout.write(self.style.SUCCESS(
            'The all data from .csv-files are imported.')
        )
