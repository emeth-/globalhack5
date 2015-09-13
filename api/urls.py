from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_info_special$', "api.views.get_info"),

    url(r'^contact_received$', "api.views.contact_received"),
    
    url(r'^contact_received_voice$', "api.views.contact_received_voice"),

)