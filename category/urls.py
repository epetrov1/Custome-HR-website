from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.category_list, name='category'),
]
