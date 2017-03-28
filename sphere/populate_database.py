#! /usr/bin/ python
# -*- coding: utf-8 -*-

import os
import sys
import uuid
import random
#import pymysqlclient
import MySQLdb
import random
#pymysql.install_as_MySQLdb()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sphere.settings")

import django
django.setup()

from myproject.models import Course, Professor, LikeModel, Comment, Faculty 
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.conf import settings
N = 1000
SUBJECT = set(['психологию_', 'история_', 'физика_', 'математик_', 'биология_', 'экономика_'])
	
def add_data():
	Course.objects.all().delete()
	Faculty.objects.all().delete()
	Professor.objects.all().delete()
	Comment.objects.all().delete()
	LikeModel.objects.all().delete()
	course_arr = []
	comm_arr = []
	prof_arr = []
	fac_arr = []
	like_arr = []
	for i in range(1, N+1):
		length = random.randint(10, 50)
		print i
		#course_name = random.sample(set(['Введение в', 'Рассказ о', 'Начало']), 1) + random.sample(set(SUBJECT), 1) +unicode(i)
		course_name = 'Курс' #+ unicode(i)
		lector_name = 'профессор'  +  str(i)
		faculty_name = 'факультет ' + str(i)
		
		faculty = Faculty( name = faculty_name)
		
		professor = Professor( name = lector_name, faculty = faculty)
		
		course = Course(title = course_name, professor =  professor, faculty = faculty)
		
		#like_arr.append(Like(content_type = random.sample(set(['Faculty', 'Professor', 'Course'])), 1), object_id = object_id)
		object_id = random.randint(1, i )
		content_type = Faculty
		like_arr.append(LikeModel(object_id = object_id))
		content = " Комментарий"+ str(i)
		comm_arr.append(Comment(content = content))
		
		fac_arr.append(faculty)
		prof_arr.append(professor)  
		
		course_arr.append(course) 

	Faculty.objects.bulk_create(fac_arr)
	Professor.objects.bulk_create(prof_arr)
	Course.objects.bulk_create(course_arr)
	Comment.objects.bulk_create(comm_arr)
	LikeModel.objects.bulk_create(like_arr)	
if __name__ == '__main__':
    add_data()	
	
