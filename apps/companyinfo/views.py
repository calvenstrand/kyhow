from django.shortcuts import render_to_response, get_object_or_404, redirect, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from apps.createpage.models import Company, Contact_person, Participate
from apps.companyinfo.forms import CompanyForm
from django.contrib.auth.decorators import login_required
from apps.createpage.forms import Contact_personForm

#Mainview for the page, holds form and table of contactpersons
@login_required
def companyInfo(request, company_id):

    getCompany = get_object_or_404(Company, pk=company_id)
    contactperson_list = Contact_person.objects.filter(company_id=company_id)
    #Participate_list = Participate.objects.all()
    Participate_list = Participate.objects.filter(company_id=company_id)
    
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
def editContactPerson(request, contact_person_id):
    
    getContactPerson = get_object_or_404(Contact_person, pk=contact_person_id)
    
    if request.method == "POST":
        form = Contact_personForm(request.POST, instance=getContactPerson or None)
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()
            
            return redirect('apps.companyinfo.views.companyInfo', company_id=getContactPerson.company_id.id)
        
        else:
            return render(request, "companyinfo/editContactPerson.html", {
            'Contact_personForm': form,
            'Contact_person': getContactPerson,
            })
        
        
    else:
        form = Contact_personForm(instance=getContactPerson)
        return render(request, "companyinfo/editContactPerson.html", {
        'Contact_personForm': form,
        'Contact_person': getContactPerson,
    })