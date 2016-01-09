from __future__ import unicode_literals

from django.db import models

from django.db import models

def duration_check(dur):
	if dur != 2 or dur != 8:
		return 2

class Course(models.Model):
	course_title = models.CharField(max_length=200)
	course_description = models.CharField(max_length=200)
	course_instructor = models.CharField(max_length=200)
	course_duration = models.IntegerField(default=2)
	# course_image = models.CharField(max_length=200)
	def __str__(self):
		return self.course_title + self.course_description + self.course_instructor + str(self.course_duration) + self.course_image