from django.db import models


class TrendingStuff(models.Model):
	movie = models.CharField(max_length=32)

	def __unicode__(self):
		return self.movie



class BrainSystem(models.Model):
	query = models.CharField(default=True,max_length=500)
	knowledge = models.CharField(max_length=1000)


	def __unicode__(self):
		return self.knowledge

class TorzBrain(models.Model):
	brain = models.CharField(max_length=200)

	def __unicode__(self):
		return self.brain


class URLClicks(models.Model):
	url = models.CharField(max_length=500)
	number = models.CharField(default=0, max_length=4)

	def __unicode__(self):
		return self.url


class SearchClick(models.Model):
	url = models.CharField(max_length=600)

	def __unicode__(self):
		return self.url