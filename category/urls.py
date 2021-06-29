from django.urls import path
from . import views
#from .views import CompanyOrderView

urlpatterns = [
    path('all/<int:id>/', views.category_list, name='category'),
    path('worker-apply/', views.worker_cv, name='worker_apply'),
    path('company/apply/<int:id>/', views.company_order, name='company_apply'),
    path('worker/cv/<int:id>/', views.worker_cv, name='worker_cv'),
    path('cv/detail/<int:id>/', views.cv_detail, name="cv_detail"),
    path('order/detail/<int:id>/', views.order_detail, name="order_detail"),
    path('company-apply/thanks/', views.thanks, name='thanks'),
    path('available-workers/<int:id>/', views.workers_cvs, name='workers_cvs'),

]
