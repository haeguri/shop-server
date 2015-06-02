from django.contrib import admin
from snippets.models import Gender, Product, Brand, Channel, Issue, IssueItem, \
    ProductImage, BrandInterview, HashTag, HashTagCategory

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

class ChannelAdmin(admin.ModelAdmin):

    list_display = ['id', 'maker', 'brief', 'created']

    list_editable = ['maker', 'brief']

class BrandInline(admin.StackedInline):
    model = BrandInterview

    extra = 2

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'designer', 'gender', 'web', 'address']
    list_editable = ['gender', 'designer', 'web', 'address']
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

admin.site.register(HashTagCategory, HashTagCategoryAdmin)
admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Issue, IssueAdmin)


from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from snippets.models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nickname')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'is_active', 'is_admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nickname', 'date_joined','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nickname',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)