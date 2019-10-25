from django.db import models
from uuid import uuid4


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300, blank=False, null=False)

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300, blank=False, null=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    public = models.BooleanField(default=False)
    address = models.CharField(max_length=300, blank=False, null=False)
    category = models.ManyToManyField(Category, related_name='events',
                                      related_query_name='event',
                                      blank=False)

