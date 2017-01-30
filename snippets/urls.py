from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = patterns('',
    url(r'^genders$', views.gender_list),
    url(r'^genders/(?P<gender_id>[0-9]+)/tags/(?P<tag_id>[0-9]+)/products$', views.product_list),
    url(r'^genders/(?P<gender_id>[0-9]+)/tags/(?P<tag_id>[0-9]+)/products/(?P<product_id>[0-9]+)$', views.product_detail),
    url(r'^genders/(?P<gender_id>[0-9]+)/brands?$', views.brand_list),
    url(r'^genders/(?P<gender_id>[0-9]+)/brands/(?P<brand_id>[0-9]+)$', views.brand_detail),
    # channel_detail = cody_list
    url(r'^channels/(?P<channel_id>[0-9]+)$', views.channel_detail),
    # cody list of cody category.
    url(r'^codies$', views.cody_list),
    url(r'^cody-categories/(?P<category_id>[0-9]+)/codies$', views.category_cody_list),
    url(r'^channels/(?P<channel_id>[0-9]+)/codies/(?P<cody_id>[0-9]+)$', views.cody_detail),
    url(r'^users/(?P<user_id>[0-9]+)/cart$', views.cart_list),
    url(r'^users/(?P<user_id>[0-9]+)$', views.user_detail),
    url(r'^users/(?P<user_id>[0-9]+)/products/(?P<product_id>[0-9]+)/like$', views.product_like),
    url(r'^users/(?P<user_id>[0-9]+)/codies/(?P<cody_id>[0-9]+)/like$', views.cody_like),
    url(r'^users/(?P<user_id>[0-9]+)/channels/(?P<channel_id>[0-9]+)/follow', views.channel_follow),
    url(r'^users/(?P<user_id>[0-9]+)/brands/(?P<brand_id>[0-9]+)/follow$', views.brand_follow),
)

urlpatterns = format_suffix_patterns(urlpatterns)