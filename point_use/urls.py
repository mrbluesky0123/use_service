from django.conf.urls import url 
from use_service import views

urlpatterns = [ 
    url(r'^toys/$', views.toy_list), 
    url(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail), 
] 