from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^detail/(?P<slug>[-\w]+)$', views.post_detail, name="detail"),
    url(r'^signup/$', views.usersignup, name="signup"),
    url(r'^login/$', views.userlogin, name="login"),
    url(r'^logout/$', views.userlogout, name="logout"),
    url(r'^like_botton/(?P<post_id>[\d]+)/$', views.like_botton, name="like_botton"),
    url(r'^search_bar/$', views.search_bar, name="search_bar"),


    url(r'^create/$', views.post_create, name="create"),
    
    url(r'^list/$', views.post_list, name="list"),
    url(r'^update/(?P<slug>[-\w]+)$', views.post_update, name="update"),
    url(r'^delete/(?P<slug>[-\w]+)$', views.post_delete, name="delete"),
    url(r'^home/$', views.post_home, name="home"),
]
