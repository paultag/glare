from django.template.loader import get_template
from django.template import Context

from glass.models import DeletableGlassTimelineItem, NotifiableGlassTimelineItem, PinableGlassTimelineItem


class TemplatedTimelineItem(DeletableGlassTimelineItem, NotifiableGlassTimelineItem):
    TEMPLATE = None
    BUNDLE = None
    COVER = False

    def __init__(self, **kwargs):
        if self.TEMPLATE is None:
            raise NotImplementedError("Erm, can't find the template")

        html = render_html(self.TEMPLATE, **kwargs)
        kwargs = {"html": html}

        if self.BUNDLE is not None:
            kwargs['bundleId'] = self.BUNDLE

        if self.COVER is not None:
            kwargs['isBundleCover'] = self.COVER

        super(TemplatedTimelineItem, self).__init__(**kwargs)


class LegislatorTimelineItem(TemplatedTimelineItem):
    TEMPLATE = "glare/cards/legislator.html"
    BUNDLE = "sunlight-glare"
    COVER = False


class LegislatorCoverItem(TemplatedTimelineItem):
    TEMPLATE = 'glare/cards/cover.html'
    BUNDLE = "sunlight-glare"
    COVER = True


def render_html(path, **kwargs):
    return get_template(path).render(Context(kwargs))
