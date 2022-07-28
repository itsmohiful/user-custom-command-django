from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Used to delete user form database'


    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='enter user id')

        #nargs multiple
    
    def handle(self, *args, **kwargs):
        users = kwargs['user_id']

        for user_id in users:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write("'%s (%s)' has been deleted!" % (user.username, user.id))

            except User.DoesNotExist:
                self.stdout.write("User '%s' does not exist! " % (user_id))
