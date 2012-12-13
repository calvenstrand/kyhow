from django.forms import ModelForm
from apps.createpage.models import Student

class EditStudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('schoolclass_id', 'course')