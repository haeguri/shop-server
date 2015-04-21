from django import forms
from snippets.models import Product, HashTagCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'hash_tags',)


    def clean(self):
        hash_tags = self.cleaned_data.get('hash_tags')
        if hash_tags is not None:
            input_categories = set(HashTagCategory.objects.filter(hashtag__id__in=hash_tags).filter(is_required=True))
            require_categories = set(HashTagCategory.objects.filter(is_required=True))

            if require_categories.difference(input_categories):
                difference_categories = list(require_categories.difference(input_categories))
                require_categories = ''
                for category in difference_categories:
                    require_categories = require_categories + ' ' + category.name

                raise forms.ValidationError("이런!!! 다음과 같은 필수 해쉬 태그를 입력하지 않았습니다. < %s >" % require_categories)

            return self.cleaned_data