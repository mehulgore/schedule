from django.conf.urls import include, url 
from . import views 

app_name = 'schedule'

urlpatterns = [
	# /sched/
    url(r'^input/$', views.InputView.as_view(), name='index'), 

    url(r'^register/$', views.UserFormView.as_view(), name='register')

    # /sched/{{id}}
    # url (r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),

    # /sched/intersect
    # url(r'^intersect/$', views.intersect, name='intersect'),

    # sched/data
    # url (r'^data/$', views.data, name='data'), 

    # sched/submit
    #url (r'^submit/$', views.submit, name='submit')

]