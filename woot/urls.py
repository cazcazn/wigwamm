from django.contrib import admin
from django.contrib.auth.views import login
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from listings.views import HomeView, ListingView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new/$', ListingView.as_view(), name='new'),
    url(r'^photologue/', include('photologue.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
