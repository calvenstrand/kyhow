from django.forms import ModelForm, forms
from apps.createpage.models import Student, Participate_Step

class EditStudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('schoolclass_id', 'course')

class EditBooleanForm(ModelForm):
    class Meta:
        model = Participate_Step
        exclude = ('name', 'description', 'participate.id')