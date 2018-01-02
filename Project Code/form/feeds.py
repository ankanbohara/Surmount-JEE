from django.contrib.syndication.views import Feed
from .models import Notification
from django.core.urlresolvers import reverse


class LatestEntriesFeed(Feed):
    title = "Educational News"
    link = "//"
    description = "Updates on changes and additions to Educational"

    @property
    def items(self):
        return Notification.objects.order_by('-pk')[:5]

    def item_title(self, item):
        return item.category

    def item_description(self, item):
        return item.notify

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('form:notification')