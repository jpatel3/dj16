from django.db import models
import datetime
from django.utils import timezone


class Post(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
    	return self.content

class Comments(models.Model):
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length=200)

    def __unicode__(self):
    	return "%s-%s"%(self.post, self.comment)