from django.urls import path
from . import views
#from .views import CompanyOrderView

urlpatterns = [
    path('all/<int:id>/', views.category_list, name='category'),
    path('jop-positions/', views.category_all, name='category_all'),
    path('worker-apply/', views.worker_cv, name='worker_apply'),
    path('company/apply/<int:id>/', views.company_order, name='company_apply'),
    path('worker/cv/<int:id>/', views.worker_cv, name='worker_cv'),
    path('cv/detail/<int:id>/', views.cv_detail, name="cv_detail"),
    path('cv/edit/<int:id>', views.edit_cv, name='edit_cv'),
    path('cv/list', views.cv_list, name='cv_list'),
    path('order/detail/<int:id>/', views.order_detail, name="order_detail"),
    path('order/edit/<int:id>', views.edit_order, name="order_edit"),
    path('order/list/', views.order_list, name='order_list'),
    path('company-apply/thanks/', views.thanks, name='thanks'),
    path('available-workers/<int:id>/', views.workers_cvs, name='workers_cvs'),
    path('partners/', views.partners, name='partners'),

]
