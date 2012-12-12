# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from apps.createpage.models import Company, Education


def companyList(request):
    education_list = Education.objects.all()

    return render_to_response('companylist/companylist.html',
        {
            'education_list': education_list
        },
        context_instance=RequestContext(request))