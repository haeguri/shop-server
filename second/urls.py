from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from second.custom_auth import FacebookLogin
from snippets.views import LadioPasswordReset, LadioPasswordChange

urlpatterns = patterns('',
    url(r'^api/', include('snippets.urls')),
    #url(r'^api/cart/', include('cart.urls')),
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/facebook/$', FacebookLogin.as_view(), name="fb_login"),
    url(r'^api/password/reset/$', LadioPasswordReset.as_view(), name="ladio_password_reset"),
    url(r'^api/password/change/$', LadioPasswordChange.as_view(), name="ladio_password_change"),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'snippets.views.ladio_password_reset_confirm', name='ladio_password_reset_confirm'),
    # url(r'^reset/$', 'snippets.views.reset', name='reset'),
    # url(r'^reset/complete/$', 'snippets.views.password_reset_complete', name='password_reset_complete'),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
]