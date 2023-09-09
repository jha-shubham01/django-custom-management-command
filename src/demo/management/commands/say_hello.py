
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This will print hello world'

    def handle(self, *args, **kwargs):
        print("Hi There!")
