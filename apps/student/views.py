from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.createpage.models import Student, Company, Contact_person
from apps.student.forms import EditStudentForm

def detailed_student(request, student_id):
    form = EditStudentForm(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()

    try:
        student_info = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return HttpResponse('Not found.')

    contact_persons = Contact_person.objects.all()

    company_list = Company.objects.all()

    return render_to_response("student/detailed_student.html", {
        'student': student_info,
        'company_list': company_list,
        'contact_persons': contact_persons,
        'edit_form': form
    }, context_instance=RequestContext(request))




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