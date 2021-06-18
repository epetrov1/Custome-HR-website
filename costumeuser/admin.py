from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User, Worker, Company

class CostumeUser(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_worker', 'is_company')
    list_filter = ('is_worker', 'is_company',)
    search_fields = ('email', 'username',)
    ordering = ('email',)

admin.site.register(User, CostumeUser)
#admin.site.register(User, UserAdmin)



class WorkerAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'first_name', 'last_name', 'phone')
admin.site.register(Worker, WorkerAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'company_name', 'address', 'phone')
admin.site.register(Company, CompanyAdmin)