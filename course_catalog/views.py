from .models import Course
from django.shortcuts import render
from django.http import HttpResponse

def courses_main(request):
	course_list = Course.objects.all()
	context = {
		'course_list': course_list,
	}
	return render(request, 'course_catalog/courses.html', context)

def courses_add(request):
	return HttpResponse('On add courses route.')

def courses_details(request, course_id):

	return HttpResponse('On course details route. Details for the following course: %s' % course_id)

def courses_change(request, course_id):
	return HttpResponse('On change course route. You may change the following course: %s' % course_id)