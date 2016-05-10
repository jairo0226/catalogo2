from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mazda.apps.home.views',
	url(r'^about/$', 'about_view', name = 'vista_about'),
	url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
) 