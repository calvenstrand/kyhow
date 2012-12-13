from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from forms import CompanyForm, Contact_personForm, CourseForm, EducationForm, SchoolclassForm, StepForm, StudentForm, TagForm

def createpage(request):
    return render_to_response("createpage/createpage.html")
    

def createschoolclass(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = SchoolclassForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = SchoolclassForm() # An unbound form

    return render(request, "createpage/createschoolclass.html", {
        'form': form,
    })
    

def createcompany(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = CompanyForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = CompanyForm() # An unbound form

    return render(request, "createpage/createcompany.html", {
        'form': form,
    })


def createcontact_person(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = Contact_personForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = Contact_personForm() # An unbound form

    return render(request, "createpage/createcontact_person.html", {
        'form': form,
    })


def createcourse(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = CourseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = CourseForm() # An unbound form

    return render(request, "createpage/createcourse.html", {
        'form': form,
    })


def createeducation(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = EducationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = EducationForm() # An unbound form

    return render(request, "createpage/createeducation.html", {
        'form': form,
    })
    

def createstep(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = StepForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = StepForm() # An unbound form

    return render(request, "createpage/createstep.html", {
        'form': form,
    })


def createstudent(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = StudentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = StudentForm() # An unbound form

    return render(request, "createpage/createstudent.html", {
        'form': form,
    })


def createtag(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = TagForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/createpage/') # Redirect after POST
    else:
        form = TagForm() # An unbound form

    return render(request, "createpage/createtag.html", {
        'form': form,
    })


