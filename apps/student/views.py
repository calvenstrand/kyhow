from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.createpage.models import Student, Participate_Step
from apps.student.forms import EditStudentForm
from django.contrib.auth.decorators import login_required

@login_required
def detailed_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    participate = Participate_Step.objects.filter(participate__student_id=student.id)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=student or None)
        if form.is_valid():
            a = form.save(commit=False)
            a.save()
        return render_to_response('student/detailed_student.html', {
            'form': form,
            'participate': participate,
            'student': student
        }, context_instance=RequestContext(request))
    else:
        form = EditStudentForm(instance=student or None)
        return render_to_response('student/detailed_student.html', {
            'form': form,
            'participate': participate,
            'student': student
        }, context_instance=RequestContext(request))