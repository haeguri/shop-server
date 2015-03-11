from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('',
    url(r'^category/(?P<gender_id>[0-9]+)/?$', views.category_list),
    url(r'^tag/(?P<gender_id>[0-9]+)/?$', views.tag_list),
    url(r'^product/?$', views.product_list),
    url(r'^product/(?P<product_id>[0-9]+)/?$', views.product_detail),


    url(r'^category/(?P<gender_id>[0-9]+)/?$', views.category_list),
    url(r'^tag/(?P<gender_id>[0-9]+)/?$', views.tag_list),
    url(r'^product/?$', views.product_list),
    url(r'^product/(?P<product_id>[0-9]+)/?$', views.product_detail),
    url(r'^cart/?$', views.cart_list),
    url(r'^designer/?$', views.designer_list),
    url(r'^designer/(?P<designer_id>[0-9]+)/?$', views.designer_detail),
    url(r'^channel/cody/?$', views.channel_cody_list),
    url(r'^channel/(?P<channel_id>[0-9]+)/?$', views.channel_detail),
    url(r'^channel/(?P<channel_id>[0-9]+)/cody/?$', views.cody_list),
    url(r'^channel/(?P<channel_id>[0-9]+)/cody/(?P<cody_id>[0-9]+)/?$', views.cody_detail),

    url(r'^user/(?P<user_id>[0-9]+)/product/(?P<product_id>[0-9]+)/like/?$', views.product_like),

    url(r'^user/(?P<user_id>[0-9]+)/?$', views.user_data),
)

urlpatterns = format_suffix_patterns(urlpatterns)