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
    url(r'^createpage/', 'apps.createpage.views.createpage'),
)
