# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from models import Course, LikeModel, Professor
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .forms import RegistrationForm, FacultyForm, CourseForm, ProfessorForm
from .models import User, Faculty, Comment
from django.contrib.contenttypes.models import ContentType


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_course = Course.objects.all().count()
    course_list = Course.objects.all()
    num_likes=LikeModel.objects.all().count()
    num_prof = Professor.objects.all().count()
    num_fac = Faculty.objects.all().count()
    #num_instances=.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_course':num_course, 'num_prof':num_prof, 'num_fac':num_fac},
    )
# Create your views here.

class CourseListView(generic.ListView):
    model = Course

class CourseDetailView(generic.DetailView):
    model = Course

class ProfessorListView(generic.ListView):
    model = Professor

class ProfessorDetailView(generic.DetailView):
    model = Professor
    

def add_professor(request):
	professors = Professor.objects.all()
	form = ProfessorForm(request.POST)
	if form.is_valid():
		form.save()
		form = ProfessorForm()
	return render(
        request, 'add_professor.html',
        {'professors': professors, 'form': form})
        
def add_course(request):
	courses = Course.objects.all()
	form = CourseForm(request.POST)
	if form.is_valid():
		form.save()
		form = CourseForm()
	return render(
        request, 'add_course.html',
        {'courses': courses, 'form': form})
        
def course_list(request):
	courses = Course.objects.all()

	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseForm()
	else:
		form = CourseForm()
        
	return render(
        request, 'course_list.html',
        {'courses': courses, 'form': form})


def course_detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id) 
    except Course.DoesNotExist:
        raise Http404('No such faculty')
    professor = course.professor
    time = course.time
    place = course.place
    faculty = course.faculty
    content_type = ContentType.objects.get_for_model(Course)

    likes = LikeModel.objects.filter( content_type=content_type, object_id = course_id)
    comments = Comment.objects.filter(content_type=content_type, object_id = course_id)
    return render(request,
    'course_detail.html', {'course':course,'professor':professor, 'time':time, 'likes':likes, 'comments': comments, 'place':place, 'faculty':faculty})

def professor_list(request):
	professors = Professor.objects.all()

	if request.method == 'POST':
		form = ProfessorForm(request.POST)
		if form.is_valid():
			form.save()
			form = ProfessorForm()
	else:
		form = ProfessorForm()
        
	return render(
        request, 'professor_list.html',
        {'professors': professors, 'form': form})

def professor_detail(request, professor_id):
    try:
        professor = Professor.objects.get(id=professor_id) 
    except Professor.DoesNotExist:
        raise Http404('No such faculty')
    courses = professor.courses.all()
    content_type = ContentType.objects.get_for_model(Professor)

    likes = LikeModel.objects.filter( content_type=content_type, object_id = professor_id)
    comments = Comment.objects.filter(content_type=content_type, object_id = professor_id)
    return render(request,
    'professor_detail.html', {'professor':professor, 'courses':courses, 'likes':likes, 'comments' : comments})
class RegisterFormView(FormView):
    form_class = RegistrationForm#UserCreationForm
	
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
        

def faculty_list(request):
    faculties = Faculty.objects.all()[:20]
    content_type = ContentType.objects.get_for_model(Faculty)
    faculty = Faculty.objects.get(id=1)
    likes = LikeModel.objects.filter( content_type=content_type, object_id = 1)
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            form = FacultyForm()
    else:
        form = FacultyForm()
        
    return render(
        request, 'faculty_list.html',
        {'faculties': faculties, 'form': form, 'likes':likes}
)


def faculty_detail(request, faculty_id):
    try:
        faculty = Faculty.objects.get(id=faculty_id) 
    except Faculty.DoesNotExist:
        raise Http404('No such faculty')
    courses = faculty.courses.all()
    content_type = ContentType.objects.get_for_model(Faculty)

    likes = LikeModel.objects.filter( content_type=content_type, object_id = faculty_id)
    comments = Comment.objects.filter(content_type=content_type, object_id = faculty_id)
    return render(request, 
    'faculty_detail.html', {'faculty':faculty, 'courses':courses, 'likes':likes, 'comments':comments})
    #result = '<h1>{0}</h1>'.format(faculty.name)
    #courses = faculty.courses.all()
    #for course in courses:
        #result += '<h2>{0}</h2>'.format(course.title)
	#return HttpResponse(result)
