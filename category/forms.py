from django.forms import ModelForm, widgets
from django import forms
from .models import CompanyOrder, Cv


#Costume widget for a datefields
class DateInput(forms.DateInput):
   input_type = 'date'


# Form for reqesting a offer from company for workers
class CompanyOrderForm(ModelForm):
   class Meta:
      widgets = {'start_date': DateInput, 'end_date': DateInput}
      model = CompanyOrder
      fields = ['country', 'city', 'address', 'workers_number', 'start_date', 'end_date']


# CV form for specific subcategory
class CvForm(ModelForm):
   class Meta:
      widgets = {
      'birth_day': DateInput, 
      'ready_to_start': DateInput, 
      'start_date_1': DateInput, 
      'start_date_2': DateInput, 
      'start_date_3': DateInput,
      'end_date_1': DateInput, 
      'end_date_2': DateInput,
      'end_date_3': DateInput,
      }
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
         'expectet_salary', 
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
      
