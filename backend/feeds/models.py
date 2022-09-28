from asyncore import read
from this import d
from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    followers = models.ManyToManyField('accounts.User', related_name='feeds',
    blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField()
    read = models.ManyToManyField('accounts.User', related_name='items',
    blank=True)
    feed = models.ForeignKey(Feed, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def is_read(self, user):
        return user in self.read.all()
    
    