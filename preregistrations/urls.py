from django.conf.urls import url

from .views import *
urlpatterns = [
				url(r'^$', views.index, name="home"),
				url(r'^/payment', views.apirequest, name="API Request")
				]