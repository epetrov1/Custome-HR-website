from django.shortcuts import render
from .forms import CompanyOrderForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from costumeuser.decorators import worker_required, company_required
from . models import Category, SubCategory

def category_list(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.select_related('category')
    context = {
        'category': category,
        'subcategory': subcategory,
    }
    return render(request, 'category/category_list.html', context)

@login_required
@worker_required
def worker_cv(request):
    return render(request, 'category/worker_form.html', {})


@login_required
@company_required
def company_order(request):
    return render(request, 'category/company_form.html', {})

class CompanyOrderView(FormView):
    form_class = CompanyOrderForm
    template_name = 'category/company_form.html'
    success_url = '/tanks.html'