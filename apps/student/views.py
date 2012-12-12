# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.createpage.models import Student, Course

def detailed_student(request, student_id):
    print student_id
    #try:
    student_info = Student.objects.get(pk=student_id)
    #except Student.DoesNotExist:
    #    return HttpResponse('Not found.')

    return render_to_response("student/detailed_student.html",
        {'student': student_info},
        #{'course': course_info},
        #context_instance=RequestContext(request)
    )

    # course_info = Course.objects.get(pk=student_id)




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