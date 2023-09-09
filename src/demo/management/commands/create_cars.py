
from django.core.management.base import BaseCommand
from demo.models import Car

CarChoices = [c[0] for c in Car.ManufacturerChoices.choices]

class Command(BaseCommand):
    help = 'This will create cars'

    def add_arguments(self, parser):
        parser.add_argument("manufacturer", type=str, choices=CarChoices, help="Number of data you want to create")


        # Optional argument
        parser.add_argument(
            '--number_of_cars',
            type=int,
            default=1,
            help='INumber of data you want to create'
        )

    
    def handle(self, *args, **kwargs):
        manufacturer = kwargs["manufacturer"]
        number_of_cars = kwargs["number_of_cars"]
        
        cars_list = []
        for car in range(number_of_cars):
            cars_list.append(Car(manufacturer=manufacturer, model_name=f"Car{car}"))
        
        Car.objects.bulk_create(cars_list)
        print(f"Successfully created {number_of_cars} of cars")
