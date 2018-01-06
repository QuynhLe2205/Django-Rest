# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=45)
	supervisor = models.CharField(max_length=45)
	duration = models.CharField(max_length=4)
	credit = models.PositiveSmallIntegerField()
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=45)
	studentid = models.CharField(max_length=8)
	group = models.CharField(max_length=10)
	def __str__(self):
		return self.name