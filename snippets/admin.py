from django.contrib import admin
from snippets.models import Gender, Category, Product#, Channel

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','pub_date','category')

    list_filter = ['category']

    search_fields = ['name']


admin.site.register(Gender)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
#admin.site.register(Channel)