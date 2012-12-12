# Create your views here.
from apps.createpage.models import Student
from django.shortcuts import render_to_response

def detailed_student(request):
    return render_to_response("template/student/detailed_student.html",

    )