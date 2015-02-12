from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('',
    url(r'^user/(?P<user_id>[0-9]+)/?$', views.user_data),
    url(r'^category/?$', views.category_list),
    url(r'^user/(?P<user_id>[0-9]+)/product/?$', views.product_list),
    url(r'^user/(?P<user_id>[0-9]+)/product/(?P<product_id>[0-9]+)/?$', views.product_detail),
    url(r'^user/(?P<user_id>[0-9]+)/product/(?P<product_id>[0-9]+)/like/?$', views.product_like),
    url(r'^user/(?P<user_id>[0-9]+)/cart/?$', views.cart_view),
    url(r'^user/(?P<user_id>[0-9]+)/cart/init/?$', views.cart_init),
    url(r'^user/(?P<user_id>[0-9]+)/cart/item/?$', views.item_of_cart),
)

urlpatterns = format_suffix_patterns(urlpatterns)