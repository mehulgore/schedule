from django.conf.urls import include, url 
from . import views 

urlpatterns = [
	# /sched/
    url(r'^$', views.index, name='index'), 

    # /sched/{{id}}
    url (r'^(?P<sched_id>[0-9]+)/$', views.detail, name='detail'),

    # /sched/update 
    url(r'^update/$', views.update, name='update'),

    # /sched/intersect
    url(r'^intersect/$', views.intersect, name='intersect'),
  
]