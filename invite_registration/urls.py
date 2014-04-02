# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from invite_registration import views
from django.views.generic import TemplateView

urlpatterns = patterns('',                                
    url(r'^invite/$', views.invite, name='invitation_invite'), 
    url(r'^request/$', views.request_invite, name='invitation_request'),
    url(r'^invite/complete/$',
        TemplateView.as_view(template_name='invite_registration/invitation_complete.html'),
        name='invitation_complete'),
    )
