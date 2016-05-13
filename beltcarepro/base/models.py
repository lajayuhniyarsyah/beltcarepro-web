from __future__ import unicode_literals
from django.contrib import admin

from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False)
	description = models.TextField()
	CO_TYPE = (
		('pt','PT'),
		('cv','CV'),
	)
	co_type = models.CharField(max_length=50, choices=CO_TYPE, blank=False)
	active = models.BooleanField(default=True)

	def create(self):
		return True
		
	def __unicode__(self):
		return self.name

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'co_type', 'active') 

class Site(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False)
	description = models.TextField()
	active = models.BooleanField()

	customer = models.ForeignKey('Customer', on_delete=models.PROTECT, related_name='sites')

	def create(self):
		return True

	def update(self):
		return True

	def in_active(self):
		return True

	def delete(self):
		return True

class Area(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False)
	description = models.TextField()
	active = models.BooleanField()

	site = models.ForeignKey('Site', on_delete=models.PROTECT, related_name='areas')

	def create(self):
		return True

class Conveyor(models.Model):
	code = models.CharField(max_length=20, blank=False)
	description = models.TextField()
	active = models.BooleanField()
	# status = function
	layout = models.ImageField()

	site = models.ForeignKey('Site', on_delete=models.PROTECT, related_name='conveyors')
	area = models.ForeignKey('Area', on_delete=models.PROTECT, related_name='conveyors')

	def create(self):
		return True

class ConveyorAsset(models.Model):
	code = models.CharField(max_length=20, blank=False)
	description = models.TextField()
	active = models.BooleanField()
	STATUS = (
		('good','good'),
		('lvl1','lvl1'),
		('lvl2','lvl2'),
		('lvl3','lvl3'),
		('lvl4','lvl4'),
	)
	status = models.CharField(max_length=50, choices=STATUS)
	installed_date = models.DateField(blank=False)

	# part = models.ForeignKey('Part')
	conveyor = models.ForeignKey('Conveyor', blank=False, on_delete=models.PROTECT, related_name='assets')
	brand = models.ForeignKey('BrandList', on_delete=models.PROTECT)

	def create(self):
		return True

class Brandlist(models.Model):
	name =  models.CharField(max_length=50, blank=False, unique=True)
	active = models.BooleanField() 






