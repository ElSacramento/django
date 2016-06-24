from django.db import models

class Dish(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	restaurant = models.ForeignKey('Restaurant', db_index=True)

class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	urlname = models.CharField(max_length=100)

	def _str_(self):
		return self.name
# Create your models here.
