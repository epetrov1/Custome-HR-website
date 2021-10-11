from django.forms import ModelForm, widgets
from django import forms
from .models import CompanyOrder, Cv
from django.utils.translation import gettext_lazy as _


#Costume widget for a datefields
class DateInput(forms.DateInput):
   input_type = 'date'

class DrivingCat(forms.CheckboxSelectMultiple):
   input_type = 'checkbox'

# Form for reqesting a offer from company for workers
class CompanyOrderForm(ModelForm):
   class Meta:
      widgets = {'start_date': DateInput, 'end_date': DateInput}
      model = CompanyOrder
      fields = ['country', 'city', 'address', 'workers_number', 'start_date', 'end_date']



# CV form for specific subcategory
class CvForm(ModelForm):

   #driving_category = forms.MultipleChoiceField(choices=DRIVING_CATEGORY, widget=DrivingCat, required=False)   
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
      'driving_category': DrivingCat,
      }

      model = Cv
      fields = [
         'cv_img',
         'birth_day', 
         'gender', 
         'driving_license',
         'driving_category',
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
         'position_1',
         'start_date_1',
         'end_date_1',
         'country_2',
         'company_name_2',
         'position_2',
         'start_date_2',
         'end_date_2',
         'country_3',
         'company_name_3',
         'position_3',
         'start_date_3',
         'end_date_3'
      ]
      
