import email

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create random user"

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='number of user you want to create.')
        parser.add_argument('-a', '--admin', action='store_true', help='Define admin account')


    def handle(self, *args, **kwargs):
        quantity = kwargs['quantity']
        admin = kwargs['admin']

        for i in range(quantity):
            username = get_random_string(15)
            password = get_random_string(8)

            if admin:
                User.objects.create_superuser(username=username, email='', password=password)

                self.stdout.write("Super User '%s (%s)' has been created!" %(username, password))
            else:
                User.objects.create_user(username=username, email='', password=password)
            
                self.stdout.write("User '%s (%s)' has been created!" %(username, password))
