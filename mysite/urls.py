from django.conf.urls import patterns, include, url
from views import hello, home, current_datetime
import books.views
import contact.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', home),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^books/search/$', books.views.search),
    url(r'^contact/$', contact.views.contact),
    url(r'^contact/thanks/$', contact.views.thanks),
)
