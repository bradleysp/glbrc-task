from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    color = models.CharField(max_length=255)
    default_status = models.BooleanField()

    def __str__(self):
        return self.name

class UserApps(models.Model):
    user = models.ForeignKey(User)
    app = models.ForeignKey('Application')
    status = models.BooleanField()

    class Meta:
        unique_together = ('user', 'app')

    def __str__(self):
        return "{0}:{1}:{2}".format(self.user, self.app, self.status)
