from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from apps.createpage.models import Company, Contact_person, Participate
from apps.companyinfo.forms import CompanyForm, EditCompanyForm
from django.contrib.auth.decorators import login_required


#Mainview for the page, holds form and table of contactpersons
@login_required
def companyInfo(request, company_id):

    getCompany = get_object_or_404(Company, pk=company_id)
    contactperson_list = Contact_person.objects.filter(company_id=company_id)
    Participate_list = Participate.objects.all()
    if request.method == "POST":

        form = CompanyForm(request.POST, instance=getCompany or None)
        answer = 0
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
            answer = 1
        return render_to_response('companyinfo/companyinfo.html',
            {'companyform': form
            ,'company': getCompany
            ,'contactperson_list': contactperson_list
            ,'Participate_list': Participate_list
            ,'answer' : answer
            }
            , context_instance=RequestContext(request))

    else:
        form = CompanyForm(instance=getCompany)
        return render_to_response('companyinfo/companyinfo.html',
            {'companyform': form
            ,'company': getCompany
            ,'contactperson_list': contactperson_list
            ,'Participate_list': Participate_list
            }
            , context_instance=RequestContext(request))





@login_required
def companyContact(request, company_id):

    getCompany = get_object_or_404(Company, pk=company_id)
    contactperson_list = Contact_person.objects.filter(company_id=company_id)
    Participate_list = Participate.objects.all()
    if request.method == "POST":

        form = EditCompanyForm(request.POST, instance=contactperson_list or None)
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
        return render_to_response('companyinfo/editcompanyinfo.html',
            {'companycontactform': form
            ,'companycontactform': contactperson_list
            ,'contactperson_list': contactperson_list
            ,'Participate_list': Participate_list
            }
            , context_instance=RequestContext(request))

    else:
        form =  EditCompanyForm(instance=contactperson_list)
        return render_to_response('companyinfo/editcompanyinfo.html',
            {'companycontactform': form
            ,'companycontactform': getCompany
            ,'contactperson_list': contactperson_list
            ,'Participate_list': Participate_list
            }
            , context_instance=RequestContext(request))




