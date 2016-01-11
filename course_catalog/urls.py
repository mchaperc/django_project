from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.courses_main, name='index'),
	url(r'^(?P<course_id>[0-9]+)/$', views.courses_details, name='details'),
	url(r'^add/$', views.courses_add, name='add'),
	url(r'^(?P<course_id>[0-9]+)/change/$', views.courses_change, name='change'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)