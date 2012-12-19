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
    courses = Course.objects.all().order_by('name')

    """
    New things for the steps

    """
    participateObjects = Participate.objects.all()
    getWantedCourse = Course.objects.latest('id') #Gets latest, should be a view to find selected also.
    participate_step = Participate_Step.objects.all().order_by('step_order')

    """
    END new things
    """

    return render_to_response("schoolclass/room.html",
        {'studentNames':student_name
            , 'class':schoolclass_id
            , 'education':education_name
            , 'courses':courses
            ,'wanted_course':getWantedCourse
            ,'participates':participateObjects
            ,'participate_step':participate_step
        },context_instance=RequestContext(request))



def make_schoolclass_participate(request, class_id, course_id):
    schoolclass = get_object_or_404(Schoolclass, pk=class_id)
    course = get_object_or_404(Course, pk=course_id)
    student_name = Student.objects.filter(schoolclass_id = schoolclass).order_by('name')


    for student in student_name:
        student.course.add(course)#Maybe check if this creates a new instance and destroys something.
        student.save()
        party2 = Participate.objects.get_or_create(course_id=course, student_id=student)
        party = get_object_or_404(Participate, course_id=course, student_id=student)
        stepsToAdd = Step.objects.filter(course_id = course)
        for step in stepsToAdd:
            Participate_Step.objects.get_or_create(name = step.name, description=step.description,step_order=step.step_order, participate=party)

        ####MIGHT NEED TESTING WHEN DEPLOYED IF IT CAN CRASH

    return redirect('apps.schoolclass.views.school_class')

@login_required
def school_class_by_course(request, course_id):
    schoolclass_id = Schoolclass.objects.all().order_by('name')
    student_name = Student.objects.all().order_by('name')
    education_name = Education.objects.all().order_by('name')
    courses = Course.objects.all().order_by('name')

    """
    New things for the steps

    """
    participateObjects = Participate.objects.all()
    getWantedCourse = get_object_or_404(Course, pk=course_id) #Gets latest, should be a view to find selected also.
    participate_step = Participate_Step.objects.all().order_by('step_order')

    """
    END new things
    """

    return render_to_response("schoolclass/room.html",
        {'studentNames':student_name
            , 'class':schoolclass_id
            , 'education':education_name
            , 'courses':courses
            ,'wanted_course':getWantedCourse
            ,'participates':participateObjects
            ,'participate_step':participate_step
        },context_instance=RequestContext(request))



