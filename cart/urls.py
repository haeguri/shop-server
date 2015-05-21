from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from cart import views


urlpatterns = patterns('',
    # http://domain.com/api/cart/로 시작하는 URL을 라우팅
    url(r'^$', views.cart_detail),

    url(r'^items$', views.cart_item_list),
    url(r'^items/(?P<item_id>[0-9]+)$', views.cart_item_detail),

    url(r'^order$', views.order),
)
urlpatterns = format_suffix_patterns(urlpatterns)