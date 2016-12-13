from django.conf.urls import url
from . import views

app_name = 'Sensordaten'
urlpatterns = [
    # /Sensordaten/
    url(r'^$', views.index, name='index'),
    # /Sensordaten jedes Nutzers, mittels ID /Sensordaten/1
    url(r'^(?P<sensorkit_id>[0-9]+)$', views.detail, name='detail'),

# /earlybirduser
#    url(r'^(?P<sensorkit_id>[0-9]+/earlybirduser/)$', views.earlybird, name='earlybird'),
]
