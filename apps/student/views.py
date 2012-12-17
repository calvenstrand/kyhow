from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.createpage.models import Student, Company, Contact_person, Participate
from apps.student.forms import EditStudentForm
from django.contrib.auth.decorators import login_required


@login_required
def detailed_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    companies = Company.objects.all()
    contact_persons = Contact_person.objects.all()
    participants = Participate.objects.all()

    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=student or None)
        if form.is_valid():
            edit_form = form.save(commit=False)
            edit_form.save()
        return render_to_response('student/detailed_student.html', {
            'companies': companies,
            'contact_persons': contact_persons,
            'edit_form': form,
            'participants': participants,
            'student': student
        }, context_instance=RequestContext(request))
    else:
        form = EditStudentForm(instance=student)
        return render_to_response('student/detailed_student.html', {
            'companies': companies,
            'contact_persons': contact_persons,
            'edit_form': form,
            'participants': participants,
            'student': student
        }, context_instance=RequestContext(request))