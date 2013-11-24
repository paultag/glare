from django.contrib.gis.db import models
from django.db.models import DateTimeField
from django.contrib.auth.models import User
from django.contrib.gis.geos import fromstr


class IssuedTimelineItem(models.Model):
    user = models.ForeignKey(User)
    cover = models.BooleanField()  # Update vs delete
    google_id = models.CharField(max_length=128)  #?


class UserLocation(models.Model):
    point = models.PointField()
    timestamp = DateTimeField()
    user = models.ForeignKey(User, unique=True)
    objects = models.GeoManager()

    @classmethod
    def from_glass_location(self, user, location):
        try:
            obj = UserLocation.objects.get(user=user)
            # slight perf. hit.
        except UserLocation.DoesNotExist:
            obj = UserLocation()

        obj.point = fromstr("POINT({lon} {lat})".format(
            lat=location.lat,
            lon=location.lon
        ))
        obj.timestamp = location.when
        obj.user = user
        return obj
