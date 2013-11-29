from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from glass.social_auth import SocialGlassAPI
from glare.cards import LegislatorTimelineItem, LegislatorCoverItem
from glare.models import UserLocation
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

        lobj = UserLocation.from_glass_location(u, latest)
        lobj.save()

        lon, lat = lobj.point.coords
        legislators = openstates.legislator_geo_search(lat, lon)

        for item in timeline:
            timeline.delete_item(item.id)

        state = legislators[0]['state'] if legislators else 'unknown'

        cover = LegislatorCoverItem(
            legs=legislators,
            state=state,
        )

        id = timeline.add_item(cover)
        for legislator in legislators:
            l = LegislatorTimelineItem(leg=legislator)
            id = timeline.add_item(l)
