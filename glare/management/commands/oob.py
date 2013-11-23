from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from glass.social_auth import SocialGlassAPI
from glare.cards import LegislatorTimelineItem
from sunlight import openstates
import uuid
import sys


class Command(BaseCommand):
    args = '<email>'
    help = 'Send a test message'

    def handle(self, email, *args, **kwargs):
        u = User.objects.get(email=email)
        api = SocialGlassAPI(u)

        timeline = api.get_timeline()
        location = api.get_location()
        latest = location.get_current_location()

        legislators = openstates.legislator_geo_search(latest.lat, latest.lon)

        for legislator in legislators:
            l = LegislatorTimelineItem(leg=legislator)
            id = timeline.add_item(l)
            print id
