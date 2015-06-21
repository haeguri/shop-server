from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from snippets.views import FacebookLogin
from snippets.views import LadioPasswordReset, LadioPasswordChange

urlpatterns = patterns('',
    url(r'^',                           include('django.contrib.auth.urls')),
    url(r'^api/',                       include('snippets.urls')),
    url(r'^accounts/',                  include('allauth.urls')),
    url(r'^api/auth/',                  include('rest_auth.urls')),
    url(r'^api/auth/registration/',     include('rest_auth.registration.urls')),
    url(r'^api/auth/facebook/$',        FacebookLogin.as_view(),                    name="fb_login"),
    url(r'^api/auth/password_reset/$',  LadioPasswordReset.as_view(),               name="ladio_password_reset"),
    url(r'^api/auth/password_change/$', LadioPasswordChange.as_view(),              name="ladio_password_change"),
    url(r'^api/auth/password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                                        'snippets.views.ladio_password_reset_confirm',name='ladio_password_reset_confirm'),

    url(r'^admin/',                     include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    # url(r'^reset/$', 'snippets.views.reset', name='reset'),
    # url(r'^reset/complete/$', 'snippets.views.password_reset_complete', name='password_reset_complete'),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
]