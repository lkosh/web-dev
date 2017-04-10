from django.conf.urls import url, include

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^courses/$', views.CourseListView.as_view(), name='courses'),
    url(r'^courses/$', views.course_list, name='course_list'),
    url(r'^add/course/$', views.add_course, name='add_course'),
  
    url(r'^course/(?P<course_id>\d+)/$', views.course_detail, name ='course_detail'),
	 
    #url(r'^course/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course-detail'),
   # url(r'^professors/$', views.ProfessorListView.as_view(), name='professors'),
   # url(r'^professor/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail'),
    url(r'^professors/$', views.professor_list, name = 'professor_list'),
	url(r'^professor/(?P<professor_id>\d+)/$', views.professor_detail, name = 'professor_detail'),
	 
    url(r'^faculties/$', views.faculty_list, name='faculty_list'),
    url(r'^faculty/(?P<faculty_id>\d+)/$', views.faculty_detail, name='faculty_detail'),
    
   # url(r'^professor/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail'),
    url(r'^add/professor$', views.add_professor, name = 'add_professor'),
]
#urlpatterns += patterns('',
    ## ...
    #(r'^search-form/$', views.search_form),
    ## ...
#)

urlpatterns += staticfiles_urlpatterns()

#from django.contrib.auth import views

urlpatterns += [
   
   url(r'^register/$', views.RegisterFormView.as_view(), name = 'register'),
]
