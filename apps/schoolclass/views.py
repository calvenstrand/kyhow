# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.createpage.models import Schoolclass, Education, Student

def school_class(request):
    schoolclass_id = Schoolclass.objects.all().order_by('name')
    student_name = Student.objects.all().order_by('name')
    education_name = Education.objects.all().order_by('name')
    return render_to_response("schoolclass/room.html",{'studentNames':student_name, 'class':schoolclass_id, 'education':education_name },context_instance=RequestContext(request))

