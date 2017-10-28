from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.authentication, name='login'),
	url(r'^$',views.home, name='home'),
]