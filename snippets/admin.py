from django.contrib import admin
from snippets.models import Gender, Product, Brand, Channel, Issue, IssueItem, \
    ProductImage, BrandInterview, HashTag, HashTagCategory, BrandFeed, PubDay
#from cart.models import Order

from snippets.forms import ProductForm

class GenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_editable = ['type']

class HashTagCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_required']
    list_editable = ['name', 'is_required']


class HashTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_editable = ['name', 'category']
    list_filter = ['name', 'category']

class PubDayAdmin(admin.ModelAdmin):

    list_display = ['id', 'day']

    list_editable = ['day']


class ChannelAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'brief', 'get_pub_days', 'created']

    list_editable = ['name', 'brief']

    filter_horizontal = ['pub_days']

    def get_pub_days(self, obj):

        return "\n".join([pub_day.day for pub_day in obj.pub_days.all()])

class BrandInline(admin.StackedInline):
    model = BrandInterview

    extra = 2

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gender', 'name', 'web', 'address']
    list_editable = ['gender', 'name', 'web', 'address']
    list_filter = ['gender']
    inlines = [BrandInline]

class IssueInline(admin.StackedInline):
    model = IssueItem

    extra = 2

class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'channel', 'get_hash_tags', 'pub_date']

    list_editable = ['title', 'channel']

    list_filter = ['channel']

    filter_horizontal = ['hash_tags']

    fieldsets = [
        ('기본정보',         {'fields':['title', 'channel', 'pub_date', 'hash_tags', 'description','image' ]})
    ]

    inlines = [IssueInline]

    def get_hash_tags(self, obj):

        return "\n".join([hash_tag.name for hash_tag in obj.hash_tags.all()])

class BrandFeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'title', 'pub_date']

    list_editable = ['title', 'pub_date']

    list_filter = ['brand']

class ProductImageInline(admin.StackedInline):

    model = ProductImage

    extra = 2


class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'brand', 'gender', 'get_hash_tags', 'price', 'pub_date']

    list_editable = ['id', 'gender', 'name', 'brand', 'price']

    search_fields = ['name']

    inlines = [ProductImageInline]

    filter_horizontal = ['hash_tags']

    fieldsets = [
        ('기본정보',         {'fields':['name', 'pub_date', 'gender','brand', 'price', 'hash_tags']}),
    ]

    form = ProductForm

    def get_hash_tags(self, obj):
        return "\n".join([hash_tag.name for hash_tag in obj.hash_tags.all()])

"""
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'means_pay', 'order_date', 'state_pay', 'state_ship']

    list_editable = ['state_pay', 'state_ship']

    search_fields = ['user']
"""

admin.site.register(HashTagCategory, HashTagCategoryAdmin)
admin.site.register(BrandFeed, BrandFeedAdmin)
admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(PubDay, PubDayAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Issue, IssueAdmin)
#admin.site.register(Order, OrderAdmin)