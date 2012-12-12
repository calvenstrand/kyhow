from django.forms import ModelForm
from apps.models import Company
class CompanyForm(ModelForm):
    class Meta:
        model = Company
article = Company.objects.get(pk=1)
form = CompanyForm(instance=article)