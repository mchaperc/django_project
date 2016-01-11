from django import forms
from .models import Course

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
# 	PrependedText, PrependedAppendedText, FormActions)

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = '__all__'