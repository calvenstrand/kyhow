from django.core.signals import request_finished
from django.dispatch import receiver
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from apps.createpage.models import Student, Company, Contact_person, Participate, Step, Participate_Step
from apps.student.forms import EditStudentForm
from django.contrib.auth.decorators import login_required


@login_required
def detailed_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    companies = Company.objects.all().order_by('name')
    contact_persons = Contact_person.objects.all().order_by('first_name')
    participants = Participate.objects.filter(student_id=student)
    participate_step = Participate_Step.objects.all().order_by('step_order')

    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=student or None)
        if form.is_valid():
            edit_form = form.save(commit=False)
            edit_form.save()
        return render_to_response('student/detailed_student.html', {
            'companies': companies,
            'contact_persons': contact_persons,
            'edit_form': form,
            'part': participate_step,
            'student': student,
            'participants': participants
        }, context_instance=RequestContext(request))
    else:
        form = EditStudentForm(instance=student)
        return render_to_response('student/detailed_student.html', {
            'companies': companies,
            'contact_persons': contact_persons,
            'edit_form': form,
            'part': participate_step,
            'student': student,
            'participants': participants
        }, context_instance=RequestContext(request))

@login_required
def change_step_value(request, participate_step_id):
    step = get_object_or_404(Participate_Step, pk=participate_step_id)
    if step.done:
        step.done = False
        step.save()

        return HttpResponse({0}, mimetype='application/json')
    else:
        step.done = True
        step.save()

            ####MIGHT NEED TESTING WHEN DEPLOYED IF IT CAN CRASH
        return HttpResponse({1}, mimetype='application/json')
    
    
@login_required
def change_participate_company(request, participate_id, company_id):
    participate = get_object_or_404(Participate, pk=participate_id)
    company = get_object_or_404(Company, pk=company_id)
    
    participate.company_id = company
    participate.contact_person_id = None
    participate.save()
    
    return HttpResponse({1}, mimetype='application/json')


@login_required
def change_participate_contact_person(request, participate_id, contact_person_id):
    participate = get_object_or_404(Participate, pk=participate_id)
    contact_person = get_object_or_404(Contact_person, pk=contact_person_id)
    
    participate.contact_person_id = contact_person
    
    participate.save()
    
    return HttpResponse({1}, mimetype='application/json')

