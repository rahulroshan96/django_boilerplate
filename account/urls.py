from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .view import register_user, index


urlpatterns = [
    url(r'^register', register_user, name='register'),
    url(r'^login', login, {'template_name':'login.html'}),
    url(r'^logout', logout, {'next_page': '/'}),
    url(r'^', index),
]