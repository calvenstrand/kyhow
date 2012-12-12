from django.forms import ModelForm, Textarea
from apps.createpage.models import Company, Tag
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('id')
        widgets = {
            'descrition': Textarea(attrs={'cols': 40, 'rows': 5}),
            }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ('id')
        widgets = {}
