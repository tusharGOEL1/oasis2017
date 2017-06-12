from __future__ import unicode_literals

from django.db import models


class Rocktaves(models.Model):

	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	phone = models.CharField(default='' , blank = False, max_length=13)
	gender = models.CharField(max_length=6)
	email_address = models.EmailField(unique=True)

	def __unicode__(self):

		return self.name

	class Meta:
		verbose_name_plural = "Rocktaves"

class StandUp(models.Model):

	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	phone = models.CharField(default='' , blank = False, max_length=13)
	gender = models.CharField(max_length=6)
	email_address = models.EmailField(unique=True)
	paid = models.BooleanField(default=False)

	def __unicode__(self):

		return self.name

	class Meta:
		verbose_name_plural = "StandUp SandBox"

class StreetDance(models.Model):

	g_leader = models.CharField(max_length=100)
	members = models.CharField(max_length=600)
	city = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	phone = models.CharField(default='' , blank = False, max_length=13)
	email_address = models.EmailField(unique=True)
	paid = models.BooleanField(default=False)

	def __unicode__(self):

		return self.g_leader

	class Meta:
		verbose_name_plural = "Street Dance"

class PitchPerfect(models.Model):

	g_leader = models.CharField(max_length=100)
	members = models.CharField(max_length=600)
	city = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	phone = models.CharField(default='' , blank = False, max_length=13)
	email_address = models.EmailField(unique=True)
	paid = models.BooleanField(default=False)

	def __unicode__(self):

		return self.g_leader

	class Meta:
		verbose_name_plural = "Pitch Perfect"

class RapWars(models.Model):

	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	phone = models.CharField(default='' , blank = False, max_length=13)
	gender = models.CharField(max_length=6)
	email_address = models.EmailField(unique=True)

	def __unicode__(self):

		return self.name

	class Meta:
		verbose_name_plural = "Rap Wars"