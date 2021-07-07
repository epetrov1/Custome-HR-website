from django.urls import path, include
from .views import FaqDetailView, FaqListView



urlpatterns = [
    path('<slug:slug>/', FaqDetailView.as_view(), name="faq-detail"),
    path('', FaqListView.as_view(), name="faq"),
]