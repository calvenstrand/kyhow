#encoding=utf-8
from django.forms import ModelForm, Textarea, forms
from apps.createpage.models import Company, Tag
class CompanyForm(ModelForm):
    #Rewriting the labels to swedish
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['phone_number'].label = 'Telefonnummer'
        self.fields['address'].label = 'Adress'
        self.fields['website'].label = 'Hemsida'
        self.fields['description'].label = 'Beskrivning'
        self.fields['education'].label = 'Utbildning'
        self.fields['education'].help_text = 'Håll ned "Control", eller "Command" på en Mac, för att välja fler än en.'
        #self.fields["education_id"].queryset = Education.objects.all().order_by('name')
        self.fields['tags'].label = 'Taggar'
        self.fields['tags'].help_text = 'Håll ned "Control", eller "Command" på en Mac, för att välja fler än en.'
        self.fields["tags"].queryset = Tag.objects.all().order_by('name')
    #Exclude id and change tag of description
    class Meta:
        model = Company
        exclude = ('id')
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 5, 'class': 'descr'}),
            }


