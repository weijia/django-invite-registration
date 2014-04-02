# -*- coding: utf-8 -*-
"""
URLconf for registration and activation, using invite_registration backend.

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

#from registration.views import ActivationView
from invite_registration.backends.invite_only import InviteOnlyBackend


urlpatterns = patterns('',                                                                                            
                       url(r'^register/$',
                           InviteOnlyBackend.as_view(),
                           name='registration_register'),                       
                       url(r'^register/closed/$',
                           direct_to_template,
                           {'template': 'invite_registration/registration_closed.html'},
                           name='registration_disallowed'),
                       (r'', include('registration.auth_urls')),
                       )
