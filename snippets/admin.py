from django.contrib import admin
from snippets.models import Gender, Category, Tag, Product, Designer \
    , Channel, CodyCategory, Cody, CodyItem

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('type', 'gender')

    list_filter = ['gender']

    search_fields = ['type']

class TagAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender', 'category')

    list_filter = ['gender']

    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','tag', 'designer', 'pub_date', 'price', 'image')

    list_filter = ['tag']

    search_fields = ['name']

class CodyCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'gender')

    list_filter = ['gender']

    search_fields = ['name']


class CodyInline(admin.StackedInline):
    model = CodyItem
    extra = 3

class CodyAdmin(admin.ModelAdmin):
    list_display = ('title', 'cody_category', 'desc', 'pub_date')

    list_filter = ['cody_category']

    fieldsets = [
        (None,         {'fields':['cody_category']}),
        (None,         {'fields':['channel']}),
        (None,         {'fields':['title']}),
        (None,        {'fields':['desc']}),
        (None,         {'fields':['image']}),
        (None,         {'fields':['pub_date']}),
    ]
    inlines = [CodyInline]

admin.site.register(Gender)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Designer)
admin.site.register(Channel)
admin.site.register(CodyCategory, CodyCategoryAdmin)
admin.site.register(Cody, CodyAdmin)