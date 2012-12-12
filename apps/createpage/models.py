from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length= 255, blank=True)
    phonenummber = models.IntegerField(blank=True)
    class_id = models.ForeignKey('Class')
    course = models.ManyToManyField('Course')
    
    def __unicode__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=60)
    education_id = models.ForeignKey('Education')
    
    def __unicode__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=60)
    descrition = models.CharField(max_length=5000, blank=True)
    companys = models.ManyToManyField('Company', blank=True)
    
    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length= 255, blank=True)
    phonenummber = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    website = models.CharField(max_length= 1000, blank=True)
    descrition = models.CharField(max_length=5000, blank=True)
    
    def __unicode__(self):
        return self.name

class Contact_person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    titel = models.CharField(max_length=200, blank=True)
    phonenummber = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    descrition = models.CharField(max_length=5000, blank=True)
    company_id = models.ForeignKey('Company')
    
    def __unicode__(self):
        return self.first_name

class Tag(models.Model):
    name = models.CharField(max_length=60)
    companys = models.ManyToManyField('Company', blank=True)
    
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=60)
    descrition = models.CharField(max_length=5000, blank=True)
    teacher = models.CharField(max_length=60, blank=True)    
    
    
    def __unicode__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=60)
    descrition = models.CharField(max_length=5000, blank=True)
    course_id = models.ForeignKey('Course')
    
    
    def __unicode__(self):
        return self.name

class Participate(models.Model):
    course_id = models.ForeignKey('Course')
    contact_person_id = models.ForeignKey('Contact_person', blank=True)
    company_id = models.ForeignKey('Company')
    

class Participate_Step(models.Model):
    name = models.CharField(max_length=60)
    descrition = models.CharField(max_length=5000, blank=True)
    done = models.BooleanField()
    participate = models.ForeignKey('Participate')
    
    def __unicode__(self):
        return self.name












