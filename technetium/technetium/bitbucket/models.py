from django.contrib.auth.models import User
from django.db import models

class Subscription(models.Model):
    """
    Django Model for repository subscriptions.
    Foreign Key on User.
    """
    user = models.ForeignKey(User)
    repository = models.CharField(max_length=80)
    slug_url = models.CharField(max_length=120)

    class Meta:
        unique_together = ('user', 'repository')
        verbose_name = "Repository Subscription"

    def __unicode__(self):
        return "%s: %s" % (self.user, self.repository)
