from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.views.generic import FormView
from apps.login.models import UserLogin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'apps.login.views.index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/(?P<student_id>\d+)/$', 'apps.student.views.detailed_student'),
    url(r'company/$', 'apps.companylist.views.companyList'),
    url(r'^company/(?P<company_id>\d+)$', 'apps.companyinfo.views.companyInfo'),
    url(r'^createpage/createschoolclass', 'apps.createpage.views.createschoolclass'),
    url(r'^createpage/createcompany', 'apps.createpage.views.createcompany'),
    url(r'^createpage/createcontact_person', 'apps.createpage.views.createcontact_person'),
    url(r'^createpage/createcourse', 'apps.createpage.views.createcourse'),
    url(r'^createpage/createeducation', 'apps.createpage.views.createeducation'),
    url(r'^createpage/createstep', 'apps.createpage.views.createstep'),
    url(r'^createpage/createstudent', 'apps.createpage.views.createstudent'),
    url(r'^createpage/createtag', 'apps.createpage.views.createtag'),    
    url(r'^createpage/', 'apps.createpage.views.createpage'),
    url(r'^company/tagsearch/', 'apps.companylist.views.companyTagSearch', name='tagsearch'),
    url(r'^company/companysearch/(?P<tag>\w+)$', 'apps.companylist.views.companiesFromSearch', name='companysearch'),
    url(r'^schoolclass/$', 'apps.schoolclass.views.school_class'),
    url(r'^schoolclass/(?P<course_id>\d+)/$', 'apps.schoolclass.views.school_class_by_course'),
    url(r'^mus/(?P<class_id>\d+)/(?P<course_id>\d+)/$', 'apps.schoolclass.views.make_schoolclass_participate'),
    url(r'^changestep/(?P<participate_step_id>\d+)/$', 'apps.student.views.change_step_value'),
    url(r'^changecompany/(?P<participate_id>\d+)/(?P<company_id>\d+)/$', 'apps.student.views.change_participate_company'),
    url(r'^changecontactperson/(?P<participate_id>\d+)/(?P<contact_person_id>\d+)/$', 'apps.student.views.change_participate_contact_person'),
    url(r'^edit/contactperson/(?P<contact_person_id>\d+)$', 'apps.companyinfo.views.editContactPerson', name='editContactPerson'),
    url(r'^edit/participate/(?P<participate_id>\d+)$', 'apps.companyinfo.views.editParticipate', name='editParticipate'),
)

urlpatterns += staticfiles_urlpatterns()
