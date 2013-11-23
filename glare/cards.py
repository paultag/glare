from django.template.loader import get_template
from django.template import Context

from glass.models import DeletableGlassTimelineItem, NotifiableGlassTimelineItem


class TemplatedTimelineItem(DeletableGlassTimelineItem, NotifiableGlassTimelineItem):
    TEMPLATE = None

    def __init__(self, **kwargs):
        if self.TEMPLATE is None:
            raise NotImplementedError("Erm, can't find the template")
        html = render_html(self.TEMPLATE, **kwargs)
        super(TemplatedTimelineItem, self).__init__(html=html)


class LegislatorTimelineItem(TemplatedTimelineItem):
    TEMPLATE = "glare/cards/legislator.html"


def render_html(path, **kwargs):
    return get_template(path).render(Context(kwargs))
