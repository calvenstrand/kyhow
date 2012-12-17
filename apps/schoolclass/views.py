# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
<<<<<<< HEAD
from apps.createpage.models import Schoolclass, Education, Student, Course
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

    for student in student_name:
        student.course.add(course)#Maybe check if this creates a new instance and destroys something.
        student.save()

    return redirect('apps.schoolclass.views.school_class')
    #return render_to_response("schoolclass/room.html",{'studentNames':student_name, 'class':schoolclass_id, 'education':education_name, 'courses':courses },context_instance=RequestContext(request))



