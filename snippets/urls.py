from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = patterns('',
    url(r'^products$', views.product_list),
    url(r'^products/(?P<product_id>[0-9]+)', views.product_detail),

    url(r'^hashtags',views.hashtag_list),
    url(r'^pubdays$', views.pubday_list),
    url(r'^channels$', views.channel_list),
    url(r'^channels/(?P<channel_id>[0-9]+)$', views.channel_detail),

    url(r'^issues$', views.issue_list),
    url(r'^issues/(?P<issue_id>[0-9]+)$', views.issue_detail),

    url(r'^brands/(?P<brand_id>[0-9]+)$', views.brand_detail),

    url(r'^feeds$', views.feed_list),

    url(r'^users/(?P<user_id>[0-9]+)$', views.user_detail),

    url(r'^users/(?P<user_id>[0-9]+)/products/(?P<product_id>[0-9]+)/like$', views.product_like),
    url(r'^users/(?P<user_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/like$', views.issue_like),
    url(r'^users/(?P<user_id>[0-9]+)/channels/(?P<channel_id>[0-9]+)/follow', views.channel_follow),
    url(r'^users/(?P<user_id>[0-9]+)/brands/(?P<brand_id>[0-9]+)/follow$', views.brand_follow),

)
urlpatterns = format_suffix_patterns(urlpatterns)