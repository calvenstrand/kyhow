from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.createpage.models import Student, Company, Contact_person
from apps.student.forms import EditStudentForm

def detailed_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, instance=student or None)
        if form.is_valid():
            edit_form = form.save(commit=False)
            edit_form.save()
        return render_to_response('student/detailed_student.html', {
            'edit_form': form,
            'student': student
        }, context_instance=RequestContext(request))
    else:
        form = EditStudentForm(instance=student)
        return render_to_response('student/detailed_student.html', {
            'edit_form': form,
            'student': student
        }, context_instance=RequestContext(request))

   # try:
   #     student_info = Student.objects.get(pk=student_id)
   # except Student.DoesNotExist:
   #     return HttpResponse('Not found.')

    #contact_persons = Contact_person.objects.all()

    #company_list = Company.objects.all()

    #return render_to_response("student/detailed_student.html", {
    ##    'student': student_info,
    #    'company_list': company_list,
    #    'contact_persons': contact_persons,
    #    'edit_form': form
    #}, context_instance=RequestContext(request))

#def companyInfo(request, company_id):
#    company_id_chosen = company_id
##    a = get_object_or_404(Company, pk=company_id_chosen)
 ##   contactperson_list = Contact_person.objects.filter(company_id=company_id_chosen)
  #  if request.method == "POST":

 ##       form = CompanyForm(request.POST, instance=a or None)
  #      if form.is_valid():
  #          cmodel = form.save()
  #          cmodel.save()
  #      return render_to_response('companyinfo/companyinfo.html',
  #          {'companyform': form
  #              ,'company': a
  #              ,'contactperson_list': contactperson_list
  #          },
  #          context_instance=RequestContext(request))##

    #else:
    #    form = CompanyForm(instance=a)
   #     return render_to_response('companyinfo/companyinfo.html',
   #         {'companyform': form
   #             ,'company': a
   #             ,'contactperson_list': contactperson_list},
   #         context_instance=RequestContext(request))

        #def detail(request, ad_id):
    #try:
    #    a = Ad.objects.get(pk=ad_id)
   # except Ad.DoesNotExist:
  #      return HttpResponse('Not found.')
 #   return render_to_response('ads/ad_detail.html', {'ad': a}, context_instance=RequestContext(request))

#@login_required
#def create(request):
    #if request.method == 'POST':
        #form = AddForm(request.POST, request.FILES or None)
       # if form.is_valid():
         #   new_ad = form.save(commit=False)
        #    new_ad.owner = request.user
       #     new_ad.created = datetime.now()
      #      new_ad.save()
     #       return HttpResponseRedirect('/ads/')
    #else:
     #   form = AddForm(request.FILES or None)

    #return render_to_response('ads/create_ads.html',
        #{'contact_form': form},
        #context_instance=RequestContext(request))