from django.urls import path, include
from .views import NewsDetailView, NewsListView



urlpatterns = [
    path('<slug:slug>/', NewsDetailView.as_view(), name="news-detail"),
    path('', NewsListView.as_view(), name="news"),
]