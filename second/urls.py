from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from second.custom_auth import FacebookLogin

urlpatterns = patterns('',
    url(r'^api/', include('snippets.urls')),
    #url(r'^api/cart/', include('cart.urls')),
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/facebook/$', FacebookLogin.as_view(), name="fb_login"),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
]