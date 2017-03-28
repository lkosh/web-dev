# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class Course(models.Model):
	FIRST = '1st'
	SECOND = '2nd'
	SEMESTER = (
	(FIRST, 'весенний'),
	(SECOND, 'осенний'),
	)
	time = models.TimeField(blank =True, null=True) 
	place = models.CharField(max_length = 100, db_index = True)
	title = models.CharField(max_length = 100, db_index=True)
	professor = models.ForeignKey('Professor',  related_name = 'courses', blank=True, null=True)
	faculty = models.ForeignKey('Faculty',  related_name='courses',  blank =True, null=True) 
	sem = models.CharField(max_length = 20, choices = SEMESTER, default = FIRST) 
	published_date = models.DateTimeField(blank=True, null=True)
	class Meta:
        	verbose_name='Курс'
       	 	verbose_name_plural='Курсы'
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __unicode__(self):
        	return self.title
        	
class Professor(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'ФИО',  unique = True)
	
	faculty = models.ForeignKey(to = 'Faculty', related_name = 'professors',  blank =True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	
	class Meta:
		verbose_name='Профессор'
		verbose_name_plural='Профессоры'
	def publish(self):
		self.published_date = timezone.now()
		self.save()    	
	def __unicode__(self):
		return self.name
		
class Faculty(models.Model):	
	VMK = 'ВМК'
	MM = 'Мехмат'
	FF = 'Физфак'
	FACULTY = (
	(VMK, 'ВМК'),
	(MM, 'Мехмат'),
	(FF, 'Физфак'),
	)
	NAT  = 'Есстеств.'
	HUM = 'Гум'
	TECH = 'Тех'
	FIELDS = (
	(NAT, 'Есстесственно-научное'),
	(HUM, u'Гуманитарное'),
	(TECH, u'Техническое'),
	)
	published_date = models.DateTimeField(blank=True, null=True)
	#course = models.ManyToMany(to=Course, blank = True, null=True)
	#professor = models.ManyToMany(to=Professor, blank = True, null=True)
	name = models.CharField(max_length = 255, blank = True, null=True, unique = True) 
	field = models.CharField(max_length = 255,choices = FIELDS, blank = True, null=True)
	
	def find_courses(self):
		return self.courses	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	class Meta:
        	verbose_name='Факультет'
        	verbose_name_plural='Факультеты'
	def __unicode__(self):
		return self.name
		
class Comment(models.Model):
	content = models.TextField(max_length = 1000, default = "Комментарий")
	creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
	creation_date = models.DateTimeField(blank=True, null=True)
	
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True, blank = True )
	object_id = models.PositiveIntegerField(null = True, blank = True)
	content_object = GenericForeignKey('content_type', 'object_id')
	
	class Meta:
        	verbose_name='Комментарий'
        	verbose_name_plural='Комментарии'
        	
	def publish(self):
		self.creation_date = timezone.now()
		self.save()
		
	def __unicode__(self):
		return unicode(self.content[:20]) 

class LikeModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank = True,
        null = True
    )
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True, blank = True )
    object_id = models.PositiveIntegerField(null = True, blank = True )
    content_object = GenericForeignKey('content_type', 'object_id')
   
    timestamp = models.DateTimeField(auto_now_add=True, blank =True, null=True)
    
    class Meta:
        	verbose_name='Лайк'
        	verbose_name_plural='Лайки'
    
    def publish(self):
        self.timestamp = timezone.now()
        self.save()
    def __unicode__(self):
       return 'Like ' + unicode(self.timestamp)
   
