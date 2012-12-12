# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from apps.createpage.models import Company

def companyInfo(request):
    info_list=Company.objects.filter(id=1)
    return render_to_response('companyinfo/companyinfo.html',
        {'info_list': info_list},
        context_instance=RequestContext(request))