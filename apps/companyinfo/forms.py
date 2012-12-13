from django.forms import ModelForm, Textarea, forms
from apps.createpage.models import Company, Tag
class CompanyForm(ModelForm):
    #Rewriting the labels to swedish
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Namn"
        self.fields['phone_number'].label = "Telnr"
        self.fields['address'].label = "Adress"
        self.fields['website'].label = "Hemsida"
        self.fields['description'].label = "Beskrivning"
        self.fields['tags'].label = "Taggar"
    #Exclude id and change tag of description
    class Meta:
        model = Company
        exclude = ('id')
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 5, 'class': 'descr'}),
            }


