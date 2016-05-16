from __future__ import unicode_literals
from django.contrib import admin
from django.core.validators import MinLengthValidator

from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False)
	description = models.TextField()
	CO_TYPE = (
		('PT','PT'),
		('CV','CV'),
	)
	co_type = models.CharField(max_length=5, choices=CO_TYPE, blank=False)
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
		
	def __unicode__(self):
		return self.name

class SiteAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'active', 'customer')

class Area(models.Model):
	name = models.CharField(max_length=50, unique=True, blank=False)
	description = models.TextField()
	active = models.BooleanField()

	site = models.ForeignKey('Site', on_delete=models.PROTECT, related_name='areas')

	def create(self):
		return True

class AreaAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'active', 'site')

class Conveyor(models.Model):
	code = models.CharField(max_length=25, blank=False)
	description = models.TextField()
	active = models.BooleanField()
	# status = function
	layout = models.ImageField()

	site = models.ForeignKey('Site', on_delete=models.PROTECT, related_name='conveyors')
	area = models.ForeignKey('Area', on_delete=models.PROTECT, related_name='conveyors')

	def create(self):
		return True

class ConveyorAdmin(admin.ModelAdmin):
	list_display = ('code', 'description', 'active', 'layout', 'site', 'area')

class ConveyorAsset(models.Model):
	code = models.CharField(max_length=14, blank=False)
	description = models.TextField()
	active = models.BooleanField()
	STATUS = (
		('good','good'),
		('lvl1','lvl1'),
		('lvl2','lvl2'),
		('lvl3','lvl3'),
		('lvl4','lvl4'),
	)
	status = models.CharField(max_length=5, choices=STATUS)
	installed_date = models.DateField(blank=False)

	part = models.ForeignKey('Part')
	conveyor = models.ForeignKey('Conveyor', blank=False, on_delete=models.PROTECT, related_name='assets')
	brand = models.ForeignKey('BrandList', on_delete=models.PROTECT)

	def create(self):
		return True

class Brandlist(models.Model):
	name =  models.CharField(max_length=50, blank=False, unique=True)
	active = models.BooleanField() 

class Part(models.Model):
	name = models.CharField(max_length=120, blank=False, unique=True)
	code = models.CharField(max_length=3, validators=[MinLengthValidator(3)], blank=False, unique=True)
	IMPORTANT_LEVEL = (
		(1,1),
		(2,2),
		(3,3),
		(4,4),
	)
	important_level = models.CharField(max_length=5, choices=IMPORTANT_LEVEL)
	POINT = (
		(10,10),
		(8,8),
		(5,5),
		(1,1),
	)
	point = models.CharField(max_length=5, choices=POINT)
	icon = models.FileField()

	depend = models.ForeignKey('Part', blank=True, related_name='childs')

	def create(self):
		return True

	def update(self):
		return True

	def delete(self):
		return True

class PartTypeList(models.Model):
	name = models.CharField(max_length=50, blank=False)
	code = models.CharField(max_length=3, blank=False)

	part = models.ForeignKey('Part', blank=False, related_name='types')

	def create(self):
		return True