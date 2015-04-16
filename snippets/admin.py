from django.contrib import admin
from snippets.models import Gender, Tag, Product, Brand \
    , Channel, CodyCategory, Cody, CodyItem, ProductSort, ProductImage, BrandInterview

class TagAdmin(admin.ModelAdmin):

    list_display = ('type', 'gender', 'category', 'slug')

    list_filter = ['gender']

    list_editable = ['slug']

    search_fields = ['type']

class ProductImageInline(admin.StackedInline):
    model = ProductImage

    extra = 3

class ProductSortAdmin(admin.ModelAdmin):

    list_display = ['type']

    list_editable = ['type']

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name','tag', 'brand', 'price', 'pub_date']

    list_editable = ['name', 'tag', 'brand', 'price']

    list_filter = ['tag']

    search_fields = ['name']

    inlines = [ProductImageInline]

class CodyCategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'gender']

    list_filter = ['gender']

    search_fields = ['name']


class CodyInline(admin.StackedInline):
    model = CodyItem

    extra = 3

class CodyAdmin(admin.ModelAdmin):
    list_display = ['title', 'cody_category', 'channel', 'description', 'which_day', 'pub_date']

    list_editable = ['cody_category', 'channel']

    list_filter = ['cody_category']

    fieldsets = [
        (None,         {'fields':['title']}),
        (None,         {'fields':['which_day']}),
        (None,         {'fields':['cody_category']}),
        (None,         {'fields':['channel']}),
        (None,        {'fields':['description']}),
        (None,         {'fields':['image']}),
        (None,         {'fields':['pub_date']}),
    ]

    inlines = [CodyInline]

class CodyCategoryAdmin(admin.ModelAdmin):
    list_display = ['gender', 'name']

    list_filter = ['gender']

    list_editable = ['name']

class BrandInline(admin.StackedInline):
    model = BrandInterview

    extra = 3

class BrandAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'name']
    list_filter = ['gender']
    list_editable = ['name']
    inlines = [BrandInline]

admin.site.register(Gender)
admin.site.register(Tag, TagAdmin)
admin.site.register(ProductSort, ProductSortAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Channel)
admin.site.register(CodyCategory, CodyCategoryAdmin)
admin.site.register(Cody, CodyAdmin)