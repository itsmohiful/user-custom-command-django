import email

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create random user"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='number of user you want to create.')


    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']

        for i in range(quantity):
            username = get_random_string(15)
            password = get_random_string(8)

            User.objects.create_user(username=username, email='', password=password)
            