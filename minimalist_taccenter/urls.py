from django.conf.urls import patterns, include, url
from django.contrib import admin
from agents_status_notifier.views import AgentStatusView


urlpatterns = [
    url(r'^agentstatus$', AgentStatusView.as_view())
]
