# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponse
from django.template import RequestContext
from apps.createpage.models import Company, Education, Tag
from django.utils.simplejson import dumps, loads, JSONEncoder


def companyList(request):
    education_list = Education.objects.all()

    return render_to_response('companylist/companylist.html',
        {
            'education_list': education_list

        },
        context_instance=RequestContext(request))

def companiesFromSearch(request, tag):
    filter_dict = {'tags__name__icontains': tag}
    matched_companies_list = Company.objects.filter(**filter_dict)
    return render_to_response('companylist/companyfromsearch.html',
        {
            'matched_companies_list': matched_companies_list
            ,'searchTerm': tag


        },
        context_instance=RequestContext(request))

def companyTagSearch(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        tags = Tag.objects.filter(name__icontains = q )[:20]
        results = []
        for tag in tags:
            drug_json = {}
            drug_json['label'] = tag.name
            drug_json['value'] = tag.id

            results.append(drug_json)
        data = dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
