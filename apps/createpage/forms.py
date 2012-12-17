from django.forms import ModelForm
from models import Schoolclass, Company, Contact_person, Course, Education, Step, Student, Tag

class SchoolclassForm(ModelForm):
    class Meta:
        model = Schoolclass

class CompanyForm(ModelForm):
    class Meta:
        model = Company

class Contact_personForm(ModelForm):
    class Meta:
        model = Contact_person

class CourseForm(ModelForm):
    class Meta:
        model = Course

class EducationForm(ModelForm):
    class Meta:
        model = Education
        
        

class StepForm(ModelForm):
    class Meta:
        model = Step

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ('course',)

class TagForm(ModelForm):
    class Meta:
        model = Tag




    