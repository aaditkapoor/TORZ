from django.db import models


class TrendingStuff(models.Model):
	movie = models.CharField(max_length=32)

	def __unicode__(self):
		return self.movie



class BrainSystem(models.Model):
	query = models.CharField(default=True,max_length=120)
	knowledge = models.CharField(max_length=200)


	def __unicode__(self):
		return self.knowledge

class TorzBrain(models.Model):
	brain = models.CharField(max_length=120)

	def __unicode__(self):
		return self.brain


