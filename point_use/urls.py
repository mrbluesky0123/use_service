from django.conf.urls import url 
from point_use import views

urlpatterns = [ 
    url(r'^point_use/', views.point_use_service), 
] 