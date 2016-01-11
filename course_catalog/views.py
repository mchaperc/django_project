from django.forms import modelformset_factory
from django.shortcuts import render
from django.shortcuts  import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext
from .models import Course
from .forms import CourseForm

def courses_main(request):
	course_list = Course.objects.all()
	context = {
		'course_list': course_list,
	}
	return render(request, 'course_catalog/courses.html', context)

def courses_add(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return courses_main(request)
		else:
			print form.errors
	else:
		form = CourseForm()
	return render_to_response(
			'course_catalog/course_add.html', 
			{'form': form}, 
			context
	)

def courses_details(request, course_id):
	try:
		course = Course.objects.get(pk=course_id)

	except Course.DoesNotExist:
		raise Http404('Course does not exist')
	return render(request, 'course_catalog/course_details.html', {'course': course})

def courses_change(request, course_id):
	course = Course.objects.get(pk=course_id)
	context = RequestContext(request)
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return courses_main(request)
		else:
			print form.errors
	else:
		form = CourseForm()
	return render_to_response(
			'course_catalog/course_change.html', 
			{'form': form}, 
			context
	)