from django.contrib import admin
from . models import Category, SubCategory, CompanyOrder, Cv

class CostumeCompanyOrder(admin.ModelAdmin):
    list_display = ('company', 'completed', 'job_titlle', 'country', 'city', 'address', 'workers_number', 'start_date', 'end_date', 'submit_date')
    list_filter = ('completed', 'job_titlle', 'submit_date')
    search_fields = ('company', 'job_titlle',)
    ordering = ('company',)

class CostumeCv(admin.ModelAdmin):
    list_display = ('id', 'worker', 'employ', 'job', 'ready_to_start', 'country_1', 'company_name_1', 'country_2', 'company_name_2', 'country_3', 'company_name_3')
    list_filter = ('employ', 'job', 'ready_to_start')
    search_fields = ('woker', 'job',)
    ordering = ('worker',)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CompanyOrder, CostumeCompanyOrder)
admin.site.register(Cv, CostumeCv)

