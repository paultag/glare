from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
# from glare.utils import GET, POST
from glass.social_auth import SocialGlassAPI


class Command(BaseCommand):
    args = '<email>'
    help = 'Send a test message'

    def handle(self, email, *args, **kwargs):
        u = User.objects.get(email=email)
        # print GET(u, "https://www.googleapis.com/mirror/v1/locations/latest")
        # print POST(u, "https://www.googleapis.com/mirror/v1/timeline", data={"text": "Foo"})
        api = SocialGlassAPI(u)
        print api.get('locations/latest')
