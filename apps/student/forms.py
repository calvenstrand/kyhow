from django.forms import ModelForm, forms
from apps.createpage.models import Student, Participate_Step

class EditStudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['email'].label = 'Email'
        self.fields['address'].label = 'Adress'
        self.fields['phone_number'].label = 'Telefonnummer'

    class Meta:
        model = Student
        exclude = ('schoolclass_id', 'course')

class EditBooleanForm(ModelForm):
    class Meta:
        model = Participate_Step
        exclude = ('name', 'description', 'participate.id')