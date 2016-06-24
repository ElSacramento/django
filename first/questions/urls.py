from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'questions.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^restaurants/([A-Za-z_]+)/', 'questions.views.restaurant'),
)