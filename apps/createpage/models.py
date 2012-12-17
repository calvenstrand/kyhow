from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length= 255, blank=True)
    phone_number = models.CharField(max_length= 255, blank=True)
    schoolclass_id = models.ForeignKey('Schoolclass')
    course = models.ManyToManyField('Course', blank=True)
    
    def __unicode__(self):
        return self.name


class Schoolclass(models.Model):
    name = models.CharField(max_length=60)
    education_id = models.ForeignKey('Education')
    
    def __unicode__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=5000, blank=True)
    
    
    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length= 255, blank=True)
    phone_number = models.CharField(max_length= 255, blank=True)
    email = models.EmailField(blank=True)
    website = models.CharField(max_length= 1000, blank=True)
    description = models.CharField(max_length=5000, blank=True)
    education = models.ManyToManyField('Education', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    
    def __unicode__(self):
        return self.name

class Contact_person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    title = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length= 255, blank=True)
    email = models.EmailField(blank=True)
    description = models.CharField(max_length=5000, blank=True)
    company_id = models.ForeignKey('Company')
    
    def __unicode__(self):
        return self.first_name

class Tag(models.Model):
    name = models.CharField(max_length=60)
    
    
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=5000, blank=True)
    teacher = models.CharField(max_length=60, blank=True)    
    
    
    def __unicode__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=5000, blank=True)
    course_id = models.ForeignKey('Course')
    
    
    def __unicode__(self):
        return self.name

class Participate(models.Model):
    course_id = models.ForeignKey('Course')
    contact_person_id = models.ForeignKey('Contact_person', blank=True)
    company_id = models.ForeignKey('Company', blank=True)
    student_id = models.ForeignKey('Student', blank=True)

class Participate_Step(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=5000, blank=True)
    done = models.BooleanField()
    participate = models.ForeignKey('Participate')
    
    def __unicode__(self):
        return self.name












