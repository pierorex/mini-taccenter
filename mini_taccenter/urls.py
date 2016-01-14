from django.conf.urls import patterns, include, url
from django.contrib import admin
from agents_status_notifier.views import AgentStatusView, AgentView
from callcenter.views import LoginView


urlpatterns = [
    # Add "?format=json" add the end of each DRF url 
    # because debug = False in settings.py
    url(r'^agentstatus$', AgentStatusView.as_view()),
    url(r'^agent/$', AgentView.as_view()),
    url(r'^auth$', LoginView.as_view(), name='authenticate'),
    # url(r'^logout$', LogoutView.as_view(), name='logout'),
]
