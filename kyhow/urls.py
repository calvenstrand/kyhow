from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.login.views.index'),
    url(r'^student/(?P<student_id>\d+)/$', 'apps.student.views.detailed_student'),
    url(r'^admin/', include(admin.site.urls)),
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
    url(r'^room/$', 'apps.schoolclass.views.school_class'),

)
