# stdlib
import sys

import csv

from django.core.management.base import BaseCommand
from demo.models import Car

def import_cars(cars_file):
    csv_file = open(cars_file, errors="ignore")
    reader = csv.reader(csv_file)
    cars_list = []
    for id, row in enumerate(reader):
        cars_list.append(
            Car(manufacturer=row[0], model_name=row[1])
        )

    Car.objects.bulk_create(cars_list)


class Command(BaseCommand):
    help = 'Import Cars CSV and create data'

    def add_arguments(self, parser):
        parser.add_argument("cars_file", type=str, help="Cars file csv")

    
    def handle(self, *args, **kwargs):
        if len(sys.argv) != 3:
            print('Import issue')
            sys.exit(1)

        import_cars(sys.argv[2])

        print("Successfully imported the cars")
