from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from cart import views


urlpatterns = patterns('',
    #url(r'^channels', views.channel_list),

    url(r'^users/(?P<user_id>[0-9]+)/cart$', views.cart_detail),
    url(r'^users/(?P<user_id>[0-9]+)/cart/items$', views.cart_item_list),
    url(r'^users/(?P<user_id>[0-9]+)/cart/items/(?P<cart_item_id>[0-9]+)$', views.cart_item_detail),
)
urlpatterns = format_suffix_patterns(urlpatterns)