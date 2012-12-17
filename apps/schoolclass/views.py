# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from apps.createpage.models import Schoolclass, Education, Student, Course, Participate, Contact_person, Company, Step, Participate_Step
from django.contrib.auth.decorators import login_required



@login_required
def school_class(request):
    schoolclass_id = Schoolclass.objects.all().order_by('name')
    student_name = Student.objects.all().order_by('name')
    education_name = Education.objects.all().order_by('name')
    courses = Course.objects.all().order_by('name');

    return render_to_response("schoolclass/room.html",
        {'studentNames':student_name
            , 'class':schoolclass_id
            , 'education':education_name
            , 'courses':courses
        },context_instance=RequestContext(request))


def make_schoolclass_participate(request, class_id, course_id):
    schoolclass = get_object_or_404(Schoolclass, pk=class_id)
    course = get_object_or_404(Course, pk=course_id)
    student_name = Student.objects.filter(schoolclass_id = schoolclass).order_by('name')

    ####### TO BE DELETED
    contact_person = get_object_or_404(Contact_person, pk=1)
    companiez = get_object_or_404(Company, pk=1)
    ######

    for student in student_name:
        student.course.add(course)#Maybe check if this creates a new instance and destroys something.
        student.save()
        part = Participate.objects.get_or_create(course_id=course, student_id=student, contact_person_id=contact_person, company_id=companiez)#should not need company and contact!! # We need some allow null!


    ##### newz
    party = get_object_or_404(Participate, course_id=course, student_id=student)
    stepsToAdd = Step.objects.filter(course_id = course)
    for step in stepsToAdd:
        Participate_Step.objects.get_or_create(name = step.name, description=step.description, participate=party)

    #### UPPER THINGS WORK JUST FINE, STILL NEED ALLOW NULL, MIGHT NEED TESTING WHEN DEPLOYED IF IT CAN CRASH

    return redirect('apps.schoolclass.views.school_class')



