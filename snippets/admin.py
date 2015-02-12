from django.contrib import admin
from snippets.models import Gender, Category, Product, Channel

admin.site.register(Gender)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Channel)