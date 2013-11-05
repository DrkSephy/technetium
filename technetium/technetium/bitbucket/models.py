from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    """
    Django Model for repository subscriptions.
    Foreign Key on User. Explanation and examples:
    """
    user = models.ForeignKey(User)
    repository = models.CharField(max_length=80)
    slug_url = models.CharField(max_length=120)
    owner = models.CharField(max_length=50)
    repo_id = models.IntegerField(max_length=15)
    hidden = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'repository')
        verbose_name = "Repository Subscription"

    def __unicode__(self):
        return "%s: %s" % (self.user, self.repository)
