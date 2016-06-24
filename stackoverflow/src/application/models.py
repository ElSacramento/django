from django.db import models

# class User(models.Model):
# 	login = models.CharField(max_length=255)
# 	nickname = models.CharField(max_length=255)
# 	email = models.CharField(max_length=255)
# 	password = models.CharField(max_length=255)

# class Tag(models.Model):
# 	title = models.CharField(max_length=255)

# 	def __unicode__(self):
# 		return self.title		

# class Question(models.Model):
# 	text = models.TextField()
# 	rate = models.IntegerField(default=0)
# 	title = models.CharField(max_length=255)
# 	creation_date = models.DateTimeField(blank=True)
# 	user = models.ForeignKey(User)
# 	tags = models.ManyToManyField(Tag)

# 	def __unicode__(self):
# 		return self.title

# class Answer(models.Model):
# 	text = models.TextField()
# 	question = models.ForeignKey(Question)
# 	creation_date = models.DateTimeField(blank=True)
# 	rate = models.IntegerField(default=0)
# 	user = models.ForeignKey(User)
# 	tags = models.ManyToManyField(Tag)

# 	class Like(models.Model):
# 		user = models.ForeignKey(User)

