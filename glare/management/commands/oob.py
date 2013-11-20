from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from glare.utils import qjson


class Command(BaseCommand):
    args = '<email>'
    help = 'Send a test message'

    def handle(self, email, *args, **kwargs):
        u = User.objects.get(email=email)
        print qjson(u, "https://www.googleapis.com/mirror/v1/locations/latest")
