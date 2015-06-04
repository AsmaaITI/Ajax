from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ajaxproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^searchpage/', 'ajaxapp.views.searchpage'),
	url(r'^register/$', 'ajaxapp.views.registerpage'),
	url(r'^register/saveperson', 'ajaxapp.views.saveperson'),
	url(r'^listall/delete/(?P<id>[0-9]+)$', 'ajaxapp.views.deletePerson'),
	url(r'^listall/$', 'ajaxapp.views.listall'),
	url(r'^listall', 'ajaxapp.views.listall'),
	url(r'^ajax', 'ajaxapp.views.ajax'),
	#url(r'', 'ajaxapp.views.searchpage'),

]
