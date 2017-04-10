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
from django.db import connection
from myproject.models import Course, Professor, LikeModel, Comment, Faculty 
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.conf import settings
N = 10
SUBJECT = set(['психологию_', 'история_', 'физика_', 'математик_', 'биология_', 'экономика_'])
	
def add_data():
	print len(connection.queries)
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
	print "quaries ", len(connection.queries)
	for i in range(1, N+1):
		length = random.randint(10, 50)
		

		faculty_name = "Факультет" + str(i)
		faculty = Faculty( name = faculty_name, id = i)		
		
		fac_arr.append(faculty)

	list_of_objects = Faculty.objects.bulk_create(fac_arr)

	prof_arr = []
	prof_fac = []
	print "quaries ", len(connection.queries)
	
	for i in range(1, N+1):
		lector_name = 'профессор'  +  str(i)
		faculty_id = random.randint(1, N-1)
		faculty = fac_arr[faculty_id]
		professor = Professor( name = lector_name, faculty = faculty, id = i)
		prof_arr.append(professor)
		
	Professor.objects.bulk_create(prof_arr)
	print "	quaries", len(connection.queries)
	
	for i in range(1, N+1):
		course_name = 'Курс' + str(i)
		prof_id = random.randint(1,N-1)
		professor = prof_arr[prof_id]
		faculty = professor.faculty
		course = Course(title = course_name, professor = professor, faculty = faculty, id = i)
		course_arr.append(course) 
		
	Course.objects.bulk_create(course_arr)
	
	for i in range(1,N+1):
		object_id = random.randint(1, N-1)
		course = course_arr[object_id]
		like_arr.append(LikeModel(content_object = course, object_id = object_id))
	LikeModel.objects.bulk_create(like_arr)	
		
	for i in range(1, N+1):
		object_id = random.randint(1, N-1)
		course = course_arr[object_id]
		content = " Комментарий"+ str(i)
		comm_arr.append(Comment(content = content, content_object = course, object_id = object_id))
	Comment.objects.bulk_create(comm_arr)
	print "	quaries", len(connection.queries)
if __name__ == '__main__':
    add_data()	
	
