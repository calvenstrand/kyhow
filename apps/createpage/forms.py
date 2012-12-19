#encoding=utf-8
from django.forms import ModelForm
from models import Schoolclass, Company, Contact_person, Course, Education, Step, Student, Tag

class SchoolclassForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SchoolclassForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['education_id'].label = 'Utbildning'

    class Meta:
        model = Schoolclass

class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['address'].label = 'Adress'
        self.fields['phone_number'].label = 'Telefonnummer'
        self.fields['email'].label = 'Email'
        self.fields['website'].label = 'Hemsida'
        self.fields['description'].label = 'Beskrivning'
        self.fields['education'].label = 'Utbildning'
        self.fields['education'].help_text = 'Håll ned "Control", eller "Command" på en Mac, för att välja fler än en.'
        self.fields['tags'].label = 'Taggar'
        self.fields['tags'].help_text = 'Håll ned "Control", eller "Command" på en Mac, för att välja fler än en.'

    class Meta:
        model = Company

class Contact_personForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Contact_personForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Förnamn'
        self.fields['last_name'].label = 'Efternamn'
        self.fields['title'].label = 'Titel'
        self.fields['phone_number'].label = 'Telefonnummer'
        self.fields['email'].label = 'Email'
        self.fields['description'].label = 'Beskrivning'
        self.fields['company_id'].label = 'Företag'

    class Meta:
        model = Contact_person

class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['description'].label = 'Beskrivning'
        self.fields['teacher'].label = 'Lärare'

    class Meta:
        model = Course

class EducationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['description'].label = 'Beskrivning'

    class Meta:
        model = Education

class StepForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StepForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['step_order'].label = 'Stegordning'
        self.fields['description'].label = 'Beskrivning'
        self.fields['course_id'].label = 'Kurs'

    class Meta:
        model = Step

class StudentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'
        self.fields['email'].label = 'Email'
        self.fields['address'].label = 'Adress'
        self.fields['phone_number'].label = 'Telefonnummer'
        self.fields['schoolclass_id'].label = 'Klass'

    class Meta:
        model = Student
        exclude = ('course',)

class TagForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Namn'

    class Meta:
        model = Tag