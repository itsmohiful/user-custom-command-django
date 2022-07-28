from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Random name genarator"

    def handle(self, *args, **kwargs):
        name = get_random_string(length=32)
        self.stdout.write(name)
