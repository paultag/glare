from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
# from glare.utils import GET, POST
from glass.social_auth import SocialGlassAPI
from glass.models import BoringGlassTimelineItem
import uuid
import sys


class Command(BaseCommand):
    args = '<email>'
    help = 'Send a test message'

    def handle(self, email, *args, **kwargs):
        u = User.objects.get(email=email)
        api = SocialGlassAPI(u)
        timeline = api.get_timeline()

        # b = BoringGlassTimelineItem(text='testing')
        # id = timeline.add_item(b)
        # print id
        # sys.stdin.readline()
        # for item in timeline:
        #     print timeline.delete_item(item.id)
