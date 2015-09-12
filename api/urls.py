from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_info_special$', "api.views.get_info"),

    url(r'^auth_first_step$', "api.views.auth_first_step"),
    
    url(r'^auth_second_step$', "api.views.auth_second_step"),

    url(r'^welcome$', "api.views.welcome"),

    url(r'^twilio$', "api.views.twilio"),
    
    url(r'^twilio_text$', "api.views.twilio_text"),
    
    url(r'^welcome_text$', "api.views.welcome_text"),
)