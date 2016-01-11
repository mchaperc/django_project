from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.db.models.fields.files import ImageField
from django.forms import ModelForm

def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)

class Course(models.Model):
	course_title = models.CharField(max_length=200)
	course_description = models.TextField()
	course_instructor = models.CharField(max_length=200)
	CHOICES=(
		('2', '2 weeks'), 
		('8', '8 weeks')
	)
	course_duration = models.CharField(max_length=100, choices=CHOICES)
	course_image = ImageField(upload_to=get_image_path, blank=True, null=True)
	def __str__(self):
		return self.course_title