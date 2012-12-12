# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from apps.createpage.models import Company
from apps.companyinfo.forms import CompanyForm

def companyInfo(request, company_id):
    if request.method == "POST":
        a = get_object_or_404(Company, pk=company_id)
        info_list=Company.objects.filter(id=company_id)
        form = CompanyForm(request.POST, instance=a or None)
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
        return render_to_response('companyinfo/companyinfo.html',
            {'info_list': info_list
                ,'companyform': form
            ,'company': a},
            context_instance=RequestContext(request))

    else:
        a = get_object_or_404(Company, pk=company_id)
        info_list=Company.objects.filter(id=company_id)
        form = CompanyForm(instance=a)
        #request.POST, instance=owner
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
        return render_to_response('companyinfo/companyinfo.html',
            {'info_list': info_list
            ,'companyform': form
            ,'company': a},
            context_instance=RequestContext(request))

