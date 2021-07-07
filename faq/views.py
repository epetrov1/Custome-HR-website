
from django.shortcuts import render
from . models import Faq
from django.views.generic import ListView, DetailView

class FaqDetailView(DetailView):
    model = Faq

class FaqListView(ListView):
    model = Faq
    ordering = ['-date_create']