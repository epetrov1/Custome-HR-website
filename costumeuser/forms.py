from . models import User, Worker, Company
from django import forms
from django.forms import ModelForm
from allauth.account.forms import SignupForm


class WorkerSignupForm(SignupForm):
    first_name = forms.CharField(label='First Name', max_length=50, required=True, strip=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, strip=True)
    phone = forms.CharField(label='Mobile phone', max_length=15, required=True, strip=True)
    def save(self, request):
        user = super(WorkerSignupForm, self).save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        # Add your own processing here.
        user.is_worker = True
        Worker.objects.create(user=user)
        user.worker.first_name = self.cleaned_data.get('first_name')
        user.worker.last_name = self.cleaned_data.get('last_name')
        user.worker.phone = self.cleaned_data.get('phone')
        user.worker.save()
        user.save()
        return user

class CompanySignupForm(SignupForm):
    company_name = forms.CharField(label='Company name', max_length=100, required=True)
    address = forms.CharField(label='Address', max_length=250, required=True)
    phone = forms.CharField(label='Mobile phone', max_length=15, required=True)
    def save(self, request):
        user = super(CompanySignupForm, self).save(request)
        user.company_name = self.cleaned_data.get('company_name')
        user.address = self.cleaned_data.get('address')
        user.phone = self.cleaned_data.get('phone')
        user.is_company = True
        Company.objects.create(user=user)
        user.company.company_name = self.cleaned_data.get('company_name')
        user.company.address = self.cleaned_data.get('address')
        user.company.phone = self.cleaned_data.get('phone')
        user.company.save()
        user.save()
        return user


class ProfileWorkerEdit(ModelForm):
    class Meta:
        model = Worker
        fields =['first_name', 'last_name', 'phone', 'image',]

class ProfileCompanyEdit(ModelForm):
    class Meta:
        model = Company
        fields =['company_name', 'address', 'phone', 'image',]