import csv

from django.core.management.base import BaseCommand
from demo.models import Car


class Command(BaseCommand):
    help = 'Export Cars CSV'

    def handle(self, *args, **options):
        with open('Cars.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [
                    "ID",
                    "Manufacturer",
                    "Model Name"
                ]
            )

            for car in Car.objects.all():
                writer.writerow(
                    [
                        car.id,
                        car.manufacturer,
                        car.model_name
                    ]
                )