from django.forms import ModelForm
from django import forms
from .models import CompanyOrder, Cv

# Create the form class.
class CompanyOrderForm(ModelForm):
   class Meta:
      model = CompanyOrder
      fields = ['country', 'city', 'address', 'workers_number', 'start_date', 'end_date']


class CvForm(ModelForm):
   class Meta:
      model = Cv
      fields = [
         'birth_day', 
         'gender', 
         'driving_license',
         'first_lang',
         'first_lang_level', 
         'second_lang', 
         'second_lang_level',
         'third_lang',
         'third_lang_level',
         'ready_to_start', 
         'sertificate_1',
         'sertificate_2',
         'country_1',
         'company_name_1',
         'start_date_1',
         'end_date_1',
         'country_2',
         'company_name_2',
         'start_date_2',
         'end_date_2',
         'country_3',
         'company_name_3',
         'start_date_3',
         'end_date_3'
      ]
      
