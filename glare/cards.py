from django.template.loader import get_template
from django.template import Context

from glass.models import DeletableGlassTimelineItem


class LegislatorTimelineItem(DeletableGlassTimelineItem):
    def __init__(self, legislator):
        pass


def render_html(path, **kwargs):
    return get_template(path).render(Context(kwargs))
