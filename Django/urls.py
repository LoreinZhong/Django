from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout
#from django.contrib import admin
#from Django.view import time
from atm import views 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#(r'^admin/',include(admin.site.urls)),
	#(r'^contact_form/$',views.contact_form),
	#(r'^search_form/$',views.search_form),
	#(r'search/$',views.search),
	(r'^login_page',views.login_page),
	(r'^login/$',views.login),
	(r'^transfer/$',views.transfer),
	(r'^save/$',views.save),
	(r'^query/$',views.query),
	(r'^draw/$',views.draw),
	(r'^exit/$',views.exit),
)
