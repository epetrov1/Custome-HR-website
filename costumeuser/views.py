from . forms import WorkerSignupForm, CompanySignupForm, ProfileWorkerEdit, ProfileCompanyEdit
from allauth.account.views import SignupView
from django.contrib.auth.decorators import login_required
from . decorators import worker_required, company_required
from . models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse





class WorkerSignUpView(SignupView):
    template_name = "costumeuser/worker_signup.html"
    form_class = WorkerSignupForm
    redirect_field_name = 'next'
    view_name = "worker_signup_view"
    success_url = None
    
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['user_type'] = "is_worker"

        return ret

worker_signup_view = WorkerSignUpView.as_view()

class CompanySignUpView(SignupView):
    template_name = "costumeuser/company_signup.html"
    form_class = CompanySignupForm
    redirect_field_name = 'next'
    view_name = "company_signup_view"
    success_url = None
    
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['user_type'] = "is_company"
        return ret

company_signup_view = CompanySignUpView.as_view()

@login_required
#@company_required
#@worker_required
def profile(request):
    user = request.user
    return render(request, "account/profile.html", {'user': user})


@login_required
@worker_required
def worker_update(request, user_id):
    user = User.objects.get(pk=user_id)
    #worker_profile = get_object_or_404(Worker, user=user)
    if request.method == "POST":
        form = ProfileWorkerEdit(request.POST, request.FILES)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name'] 
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user.worker.first_name = form.cleaned_data['first_name']
            user.worker.last_name = form.cleaned_data['last_name']
            user.worker.phone = form.cleaned_data['phone']
            user.worker.image = form.cleaned_data['image']
            user.worker.save()

            return HttpResponseRedirect(reverse('profile'))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                        'phone': user.worker.phone, 'image': user.worker.image, }
        form = ProfileWorkerEdit(default_data)

    return render(request, 'account/worker_profile.html', {'form': form, 'user': user})


def home(request):
    return render(request, 'home.html')


@login_required
@company_required
def company_update(request, user_id):
    user = User.objects.get(pk=user_id)
    #worker_profile = get_object_or_404(Worker, user=user)
    if request.method == "POST":
        form = ProfileCompanyEdit(request.POST, request.FILES)

        if form.is_valid():
            user.company.company_name = form.cleaned_data['company_name']
            user.company.address = form.cleaned_data['address']
            user.company.phone = form.cleaned_data['phone']
            user.company.image = form.cleaned_data['image']
            user.company.save()

            return HttpResponseRedirect(reverse('profile'))
    else:
        default_data = {'company_name': user.company.company_name, 'address': user.company.address,
                        'phone': user.company.phone, 'image': user.company.image, }
        form = ProfileCompanyEdit(default_data)

    return render(request, 'account/worker_profile.html', {'form': form, 'user': user})


def home(request):
    return render(request, 'home.html')