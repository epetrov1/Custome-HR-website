from django.urls import path
from . import views
from .views import CompanyOrderView

urlpatterns = [
    path('all/', views.category_list, name='category'),
    path('worker-apply/', views.worker_cv, name='worker_apply'),
    path('conpany-apply/', CompanyOrderView.as_view(), name='company_apply'),

]
