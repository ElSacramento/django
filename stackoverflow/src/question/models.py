from django.db import models
from django.conf import settings
from django.utils import timezone

class PostQuerySet(models.QuerySet):
    def best_posts(self):
        return self.order_by('-rate')
    def new_posts(self):
        return self.order_by('-creation_date')
    def posts_by_tag(self, tag):
		#kwargs['tag']=True
		#tag = kwargs['tag']
		return self.filter(tags__title__in=[tag])

class Tag(models.Model):
	title = models.CharField(max_length=255)

	def __unicode__(self):
		return self.title		

class Answer(models.Model):
	text = models.TextField()
	creation_date = models.DateTimeField(default=timezone.now)
	rate = models.IntegerField(default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.text

class Question(models.Model):
	text = models.TextField()
	rate = models.IntegerField(default=0)
	title = models.CharField(max_length=255)
	creation_date = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	tags = models.ManyToManyField(Tag, blank=True)
	answers = models.ManyToManyField(Answer, blank=True)

	objects = PostQuerySet.as_manager()

	def __unicode__(self):
		#return u"%s" % self.id
		return self.title

class Like(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	answer = models.ForeignKey(Answer)
	#question = models.ForeignKey(Question)

# Create your models here.
