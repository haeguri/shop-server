from django.contrib import admin
from snippets.models import Gender, Product, Brand, Channel, Issue, IssueItem, ProductSort, \
    ProductImage, BrandInterview, HashTag, HashTagCategory

from snippets.forms import ProductForm


class ProductImageInline(admin.StackedInline):
    model = ProductImage

    extra = 2

class ProductSortAdmin(admin.ModelAdmin):

    list_display = ['type']

    list_editable = ['type']

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'brand', 'price', 'pub_date']

    list_editable = ['name', 'brand', 'price']

    filter_horizontal = ['hash_tags']

    search_fields = ['name']

    inlines = [ProductImageInline]

    form = ProductForm

class IssueCategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'gender']

    list_filter = ['gender']

    search_fields = ['name']


class IssueInline(admin.StackedInline):
    model = IssueItem

    extra = 2

class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'channel', 'description', 'which_day', 'pub_date']

    list_editable = ['channel']

    fieldsets = [
        (None,         {'fields':['title']}),
        (None,         {'fields':['which_day']}),
        (None,         {'fields':['channel']}),
        (None,        {'fields':['description']}),
        (None,         {'fields':['image']}),
        (None,         {'fields':['pub_date']}),
    ]

    inlines = [IssueInline]

class BrandInline(admin.StackedInline):
    model = BrandInterview

    extra = 2

class BrandAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'name']
    list_filter = ['gender']
    list_editable = ['name']
    inlines = [BrandInline]

class HashTagCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_required']
    list_editable = ['is_required']


class HashTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_editable = ['category']
    list_filter = ['category']

admin.site.register(HashTagCategory, HashTagCategoryAdmin)
admin.site.register(HashTag, HashTagAdmin)


admin.site.register(Gender)
admin.site.register(ProductSort, ProductSortAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Channel)
admin.site.register(Issue, IssueAdmin)