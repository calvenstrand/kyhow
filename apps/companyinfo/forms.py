#encoding=utf-8
from django.forms import ModelForm, Textarea, forms, DateField
from apps.createpage.models import Company, Tag, Contact_person, Participate

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
        
class EditCompanyForm(ModelForm):
    #Rewriting the labels to swedish
    def __init__(self, *args, **kwargs):
        super(EditCompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['titel'].label = 'Titel'
        self.fields['phonenumber'].label = 'Telefonnummer'
        self.fields['mail'].label = 'Email'
        
        
    #Exclude id and change tag of description
    class Meta:
        model =  Contact_person
        exclude = ('id')


class ParticipateForm(ModelForm):
    #Rewriting the labels to swedish
    def __init__(self, *args, **kwargs):
        super(ParticipateForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].label = 'Start datum'
        self.fields['start_date'].help_text = 'Ex: 2006-10-25'
        self.fields['end_date'].label = 'Slut datum'
        self.fields['end_date'].help_text = 'Ex: 2006-10-25'
        self.fields['job_bool'].label = 'Jobb'
        widgets = {
            'start_date': DateField(),
        }
    
    
    class Meta:
        model = Participate
        fields = ('start_date', 'end_date', 'job_bool')