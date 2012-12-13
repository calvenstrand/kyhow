# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from apps.createpage.models import Company, Contact_person
from apps.companyinfo.forms import CompanyForm

#Mainview for the page, holds form and table of contactpersons
def companyInfo(request, company_id):

    getCompany = get_object_or_404(Company, pk=company_id)
    contactperson_list = Contact_person.objects.filter(company_id=company_id)
    if request.method == "POST":

        form = CompanyForm(request.POST, instance=getCompany or None)
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
        return render_to_response('companyinfo/companyinfo.html',
            {'companyform': form
            ,'company': getCompany
            ,'contactperson_list': contactperson_list
            }
            , context_instance=RequestContext(request))

    else:
        form = CompanyForm(instance=getCompany)
        return render_to_response('companyinfo/companyinfo.html',
            {'companyform': form
            ,'company': getCompany
            ,'contactperson_list': contactperson_list}
            , context_instance=RequestContext(request))

