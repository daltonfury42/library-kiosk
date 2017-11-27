from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.checkout, name='checkout'),
    url(r'^display.html/$', views.display, name='display'),
]
