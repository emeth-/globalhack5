from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^get_info_special$', "api.views.get_info"),
    url(r'^welcome$', "api.views.welcome"),
)