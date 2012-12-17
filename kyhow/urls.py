from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'apps.login.views.index'),
    url(r'^student/(?P<student_id>\d+)/$', 'apps.student.views.detailed_student'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'company/$', 'apps.companylist.views.companyList'),
    url(r'^company/(?P<company_id>\d+)$', 'apps.companyinfo.views.companyInfo'),
    url(r'^createpage/', 'apps.createpage.views.createpage'),
	url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()
