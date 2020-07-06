from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help =" create default group"
    def handle (self, *args, **options):
        group_list = [ 'Super Admin', 'Doctor','Examiner','Patient']
        for group in group_list:
            new_group,created = Group.objects.get_or_create(name=group)
            if created:
                self.stdout.write("Group created sucessfully")