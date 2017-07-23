from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<post_id>\d+)$', views.post_detail, name="detail"),
    
    url(r'^list/$', views.post_list, name="list"),
    url(r'^update/$', views.post_update, name="update"),
    url(r'^delete/$', views.post_delete, name="delete"),
]
