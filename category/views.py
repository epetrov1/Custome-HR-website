from costumeuser.models import User, Worker, Company
from django.shortcuts import render, redirect
from .forms import CompanyOrderForm, CvForm
from django.contrib.auth.decorators import login_required
from costumeuser.decorators import worker_required, company_required
from . models import Category, SubCategory, CompanyOrder, Cv
from django.urls import reverse
from django.http import HttpResponseRedirect


#All categorys
def category_all(request):
    category = Category.objects.all()
    return render(request, 'category/category_all.html', {'category': category})


#List of all categorys + subcategory
def category_list(request, id):
    category = Category.objects.all()
    category_1 = Category.objects.all()
    category_choise = Category.objects.get(pk=id)
    subcategory = SubCategory.objects.select_related('category').filter(category__id=id)
    context = {
        'category': category,
        'subcategory': subcategory,
        'category_choise': category_choise,
        'category_1': category_1,
    }
    return render(request, 'category/category_list.html', context)


#Partenrs page view
def partners(request):
    partners = Company.objects.all()
    return render(request, 'category/partners.html', {'partners': partners})



#Register Company making a request for workers
@login_required
@company_required
def company_order(request, id):
    subcat = SubCategory.objects.get(pk=id)

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
            comp_id = CompanyOrder.objects.all().last()
            return HttpResponseRedirect(reverse('order_detail', kwargs={'id': comp_id.id}))

            
    else:
        form = CompanyOrderForm

    return render(request, 'category/company_form.html', {'form': form, 'subcat': subcat})



#Register company editing existing objectfor applications for workers
@login_required
@company_required
def edit_order(request, id):
    order = CompanyOrder.objects.get(pk=id)
    if request.method == "POST":
        form = CompanyOrderForm(request.POST, request.FILES)

        if form.is_valid():
            order.country = form.cleaned_data['country'] 
            order.city = form.cleaned_data['city']
            order.address = form.cleaned_data['address']
            order.workers_number = form.cleaned_data['workers_number']
            order.start_date = form.cleaned_data['start_date']
            order.end_date = form.cleaned_data['end_date']
            order.save()

            return HttpResponseRedirect(reverse('order_detail', args=(id,)))
    else:
        default_data = {'country': order.country, 'city': order.city,
                        'address': order.address, 'workers_number': order.workers_number,
                        'start_date': order.start_date, 'end_date': order.end_date,
                        'update_date': order.update_date,}
        form = CompanyOrderForm(default_data)

    return render(request, 'category/company_form.html', {'form': form, 'order': order})

#Workers apply CV for specific subcategory position!
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
            cv_img = form.cleaned_data['cv_img']
            birth_day = form.cleaned_data['birth_day'] 
            gender = form.cleaned_data['gender']
            driving_license = form.cleaned_data['driving_license']
            driving_category = form.cleaned_data['driving_category']
            first_lang = form.cleaned_data['first_lang']
            first_lang_level = form.cleaned_data['first_lang_level']
            second_lang = form.cleaned_data['second_lang']
            second_lang_level = form.cleaned_data['second_lang_level']
            third_lang = form.cleaned_data['third_lang']
            third_lang_level = form.cleaned_data['third_lang_level']
            ready_to_start = form.cleaned_data['ready_to_start']
            expectet_salary = form.cleaned_data['expectet_salary']
            sertificate_1 = form.cleaned_data['sertificate_1']
            sertificate_2 = form.cleaned_data['sertificate_2']
            country_1 = form.cleaned_data['country_1']
            company_name_1 = form.cleaned_data['company_name_1']
            position_1 = form.cleaned_data['position_1']
            start_date_1 = form.cleaned_data['start_date_1']
            end_date_1 = form.cleaned_data['end_date_1']
            country_2 = form.cleaned_data['country_2']
            company_name_2 = form.cleaned_data['company_name_2']
            position_2 = form.cleaned_data['position_2']
            start_date_2 = form.cleaned_data['start_date_2']
            end_date_2 = form.cleaned_data['end_date_2']
            country_3 = form.cleaned_data['country_3']
            company_name_3 = form.cleaned_data['company_name_3']
            position_3 = form.cleaned_data['position_3']
            start_date_3 = form.cleaned_data['start_date_3']
            end_date_3 = form.cleaned_data['end_date_3']

            
            job = SubCategory.objects.get(pk=id)
            worker = User.objects.get(id=request.user.id)#request.user.id#form.instance.user = self.request.user
            Cv.objects.create(
                cv_img=cv_img,
                birth_day=birth_day,
                gender=gender,
                driving_license=driving_license,
                driving_category=driving_category,
                first_lang=first_lang,
                first_lang_level=first_lang_level,
                second_lang=second_lang,
                second_lang_level=second_lang_level,
                third_lang=third_lang,
                third_lang_level=third_lang_level,
                ready_to_start=ready_to_start,
                expectet_salary=expectet_salary,
                sertificate_1=sertificate_1,
                sertificate_2=sertificate_2,
                country_1=country_1,
                company_name_1=company_name_1,
                position_1=position_1,
                start_date_1=start_date_1,
                end_date_1=end_date_1,
                country_2=country_2,
                company_name_2=company_name_2,
                position_2=position_2,
                start_date_2=start_date_2,
                end_date_2=end_date_2,
                country_3=country_3,
                company_name_3=company_name_3,
                position_3=position_3,
                start_date_3=start_date_3,
                end_date_3=end_date_3,
                job=job,
                worker=worker,
                )
            worker_id = Cv.objects.all().last()
            
            return HttpResponseRedirect(reverse('cv_detail', kwargs={'id':worker_id.id}))


    else:
        form = CvForm

    return render(request, 'category/cv_form.html', {'form': form, 'subcat': subcat})



#CV edit just from workers
@login_required
@worker_required
def edit_cv(request, id):
    cv = Cv.objects.get(pk=id)
    if request.method == "POST":
        form = CvForm(request.POST, request.FILES)

        if form.is_valid():
            cv.cv_img = form.cleaned_data['cv_img']
            cv.birth_day = form.cleaned_data['birth_day'] 
            cv.gender = form.cleaned_data['gender']
            cv.driving_license = form.cleaned_data['driving_license']
            cv.driving_category = form.cleaned_data['driving_category']
            cv.first_lang = form.cleaned_data['first_lang']
            cv.first_lang_level = form.cleaned_data['first_lang_level']
            cv.second_lang = form.cleaned_data['second_lang']
            cv.second_lang_level = form.cleaned_data['second_lang_level']
            cv.third_lang = form.cleaned_data['third_lang']
            cv.third_lang_level = form.cleaned_data['third_lang_level']
            cv.ready_to_start = form.cleaned_data['ready_to_start']
            cv.expectet_salary = form.cleaned_data['expectet_salary']
            cv.sertificate_1 = form.cleaned_data['sertificate_1']
            cv.sertificate_2 = form.cleaned_data['sertificate_2']
            cv.country_1 = form.cleaned_data['country_1']
            cv.company_name_1 = form.cleaned_data['company_name_1']
            cv.position_1 = form.cleaned_data['position_1']
            cv.start_date_1 = form.cleaned_data['start_date_1']
            cv.end_date_1 = form.cleaned_data['end_date_1']
            cv.country_2 = form.cleaned_data['country_2']
            cv.company_name_2 = form.cleaned_data['company_name_2']
            cv.position_2 = form.cleaned_data['position_2']
            cv.start_date_2 = form.cleaned_data['start_date_2']
            cv.end_date_2 = form.cleaned_data['end_date_2']
            cv.country_3 = form.cleaned_data['country_3']
            cv.company_name_3 = form.cleaned_data['company_name_3']
            cv.position_3 = form.cleaned_data['position_3']
            cv.start_date_3 = form.cleaned_data['start_date_3']
            cv.end_date_3 = form.cleaned_data['end_date_3']

            cv.save()

            return HttpResponseRedirect(reverse('cv_detail', args=(id,)))
    else:
        default_data = {'cv_img': cv.cv_img, 'birth_day': cv.birth_day, 'gender': cv.gender,
                        'driving_license': cv.driving_license, 'driving_category': cv.driving_category, 'first_lang': cv.first_lang,
                        'first_lang_level': cv.first_lang_level, 'second_lang': cv.second_lang,
                        'second_lang_level': cv.second_lang_level, 'third_lang': cv.third_lang,
                        'third_lang_level': cv.third_lang_level, 'ready_to_start': cv.ready_to_start,
                        'expectet_salary': cv.expectet_salary, 'sertificate_1': cv.sertificate_1,
                        'sertificate_2': cv.sertificate_2, 'country_1': cv.country_1,
                        'company_name_1': cv.company_name_1, 'position_1': cv.position_1, 'start_date_1': cv.start_date_1,
                        'end_date_1': cv.end_date_1, 'country_2': cv.country_2,
                        'company_name_2': cv.company_name_2, 'position_2': cv.position_2, 'start_date_2': cv.start_date_2,
                        'end_date_2': cv.end_date_2, 'country_3': cv.country_3,
                        'company_name_3': cv.company_name_3, 'position_3': cv.position_3, 'start_date_3': cv.start_date_3,
                        'end_date_3': cv.end_date_3}
        form = CvForm(default_data)

    return render(request, 'category/cv_form.html', {'form': form, 'cv': cv})

#CV detail view after sybmit Cv form from workers: eventula query set for CV(cv = Cv.objects.get(pk=id, worker=request.user))
@login_required
def cv_detail(request, id):
    cv = Cv.objects.get(pk=id)
    workers = Worker.objects.get(pk=cv.worker_id)
    return render(request, 'category/cv_detail.html', {'cv': cv, 'workers': workers})



#List of CV's worker Applyed for job positions
@login_required
@worker_required
def cv_list(request):
    cv = Cv.objects.all().filter(worker=request.user)
    return render(request, 'category/cv_list.html', {'cv': cv})



#Order detail after submit form from a Company
@login_required
@company_required
def order_detail(request, id):
    order = CompanyOrder.objects.get(pk=id, company=request.user)
    comp = Company.objects.get(pk=order.company_id)
    return render(request, 'category/order_detail.html', {'order': order, 'comp': comp})


#List of orders for workers company request
@login_required
@company_required
def order_list(request):
    order = CompanyOrder.objects.all().filter(company=request.user)
    return render(request, 'category/order_list.html', {'order': order})


#Thanks page after submit a form: CV and CompanyOrder
def thanks(request):
    return render(request, 'thanks.html')



#List of avelable workers for specific subcategory, viewed just for companys
@login_required
@company_required
def workers_cvs(request, id):
    subcat = SubCategory.objects.get(pk=id)
    cv = Cv.objects.all().select_related('worker').filter(job_id=subcat)
    workers = User.objects.select_related('worker')
    return render(request, 'category/worker_cvs.html', {'subcat': subcat, 'cv': cv, 'workers': workers})


#SubCategory.objects.select_related('category').filter(category__id=id)