import json
import os

from django.core.management.base import BaseCommand

from backend.settings import BASE_DIR
from recipes.models import Ingredient

data_file = 'ingredients.json'
model = Ingredient


class Command(BaseCommand):
    help = 'Load data from ingredients.json to DB.'

    def handle(self, *args, **options):
        with open(
            os.path.join(BASE_DIR, 'data', data_file), encoding='utf-8'
        ) as json_file:
            data = json.load(json_file)

        for item in data:
            model.objects.get_or_create(
                name=item.get('name'),
                measurement_unit=item.get('measurement_unit'),
            )
        print(f'  Importing data from file {data_file}... OK')
        self.stdout.write(
            self.style.SUCCESS('The all data from .json-files are imported.')
        )
