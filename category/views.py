from costumeuser.models import User
from django.shortcuts import render, redirect
from .forms import CompanyOrderForm, CvForm
from django.contrib.auth.decorators import login_required
from costumeuser.decorators import worker_required, company_required
from . models import Category, SubCategory, CompanyOrder, Cv



def category_list(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.select_related('category')

    context = {
        'category': category,
        'subcategory': subcategory,
    }
    return render(request, 'category/category_list.html', context)




@login_required
@company_required
def company_order(request, id):
    subcat = SubCategory.objects.get(pk=id)
    #comp = User.objects.get(id=user.id)
    print(request, subcat.id)

    #return render(request, "category/worker_form.html", {'subcat': subcat})

    if request.method == "POST":
        form = CompanyOrderForm(request.POST)
        #subcat = SubCategory.objects.get(pk=id)
        if form.is_valid():
            country = form.cleaned_data['country'] 
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            workers_number = form.cleaned_data['workers_number']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            job_titlle = SubCategory.objects.get(pk=id)
            company = User.objects.get(id=request.user.id)#request.user.id#form.instance.user = self.request.user
            CompanyOrder.objects.create(
                country=country,
                city=city,
                address=address,
                workers_number=workers_number,
                start_date=start_date,
                end_date=end_date,
                job_titlle=job_titlle,
                company=company,
                )
            return redirect('thanks')

            
    else:
        form = CompanyOrderForm

    return render(request, 'category/company_form.html', {'form': form, 'subcat': subcat})


@login_required
@worker_required
def worker_cv(request, id):
    subcat = SubCategory.objects.get(pk=id)
    #comp = User.objects.get((id=request.user.id))

    #return render(request, "category/worker_form.html", {'subcat': subcat})

    if request.method == "POST":
        form = CvForm(request.POST, request.FILES)
        #subcat = SubCategory.objects.get(pk=id)
        if form.is_valid():
            birth_day = form.cleaned_data['birth_day'] 
            gender = form.cleaned_data['gender']
            driving_license = form.cleaned_data['driving_license']
            first_lang = form.cleaned_data['first_lang']
            first_lang_level = form.cleaned_data['first_lang_level']
            second_lang = form.cleaned_data['second_lang']
            second_lang_level = form.cleaned_data['second_lang_level']
            third_lang = form.cleaned_data['third_lang']
            third_lang_level = form.cleaned_data['third_lang_level']
            ready_to_start = form.cleaned_data['ready_to_start']
            sertificate_1 = form.cleaned_data['sertificate_1']
            sertificate_2 = form.cleaned_data['sertificate_2']
            country_1 = form.cleaned_data['country_1']
            company_name_1 = form.cleaned_data['company_name_1']
            start_date_1 = form.cleaned_data['start_date_1']
            end_date_1 = form.cleaned_data['end_date_1']
            country_2 = form.cleaned_data['country_2']
            company_name_2 = form.cleaned_data['company_name_2']
            start_date_2 = form.cleaned_data['start_date_2']
            end_date_2 = form.cleaned_data['end_date_2']
            country_3 = form.cleaned_data['country_3']
            company_name_3 = form.cleaned_data['company_name_3']
            start_date_3 = form.cleaned_data['start_date_3']
            end_date_3 = form.cleaned_data['end_date_3']

            job = SubCategory.objects.get(pk=id)
            worker = User.objects.get(id=request.user.id)#request.user.id#form.instance.user = self.request.user
            Cv.objects.create(
                birth_day=birth_day,
                gender=gender,
                driving_license=driving_license,
                first_lang=first_lang,
                first_lang_level=first_lang_level,
                second_lang=second_lang,
                second_lang_level=second_lang_level,
                third_lang=third_lang,
                third_lang_level=third_lang_level,
                ready_to_start=ready_to_start,
                sertificate_1=sertificate_1,
                sertificate_2=sertificate_2,
                country_1=country_1,
                company_name_1=company_name_1,
                start_date_1=start_date_1,
                end_date_1=end_date_1,
                country_2=country_2,
                company_name_2=company_name_2,
                start_date_2=start_date_2,
                end_date_2=end_date_2,
                country_3=country_3,
                company_name_3=company_name_3,
                start_date_3=start_date_3,
                end_date_3=end_date_3,
                job=job,
                worker=worker,
                )
            return redirect('thanks')

            
    else:
        form = CvForm

    return render(request, 'category/cv_form.html', {'form': form, 'subcat': subcat})
    

def thanks(request):
    return render(request, 'thanks.html')



def workers_cvs(request, id):
    subcat = SubCategory.objects.get(pk=id)
    cv = Cv.objects.all().filter(job_id=subcat)
    #workers = User.objects.all().filter(is_worker=True)
    return render(request, 'category/worker_cvs.html', {'subcat': subcat, 'cv': cv})
