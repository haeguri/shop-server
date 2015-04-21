from django import forms
from snippets.models import TestModel, TestHashTagCategory

class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('name', 'hash_tags',)


    def clean(self):
        hash_tags = self.cleaned_data.get('hash_tags')
        input_categories = set(TestHashTagCategory.objects.filter(testhashtag__id__in=hash_tags).filter(is_required=True))
        require_categories = set(TestHashTagCategory.objects.filter(is_required=True))

        if require_categories.difference(input_categories):
            difference_categories = list(require_categories.difference(input_categories))
            require_categories = ''
            for category in difference_categories:
                require_categories = require_categories + ' ' + category.name

            raise forms.ValidationError("이런!!! 다음과 같은 필수 해쉬 태그를 입력하지 않았습니다. < %s >" % require_categories)
        else:
            return self.cleaned_data