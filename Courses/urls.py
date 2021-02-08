from  . import views
from django.conf.urls import url


urlpatterns =[
    # /Courses/
    url(r'^$', views.index, name='index'),
    # /Courses/112/
    url(r'^(?P<Course_id>[0-9]+)/$',views.detail,name='detail'),

    ]