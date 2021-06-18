from django.forms import ModelForm
from .models import CompanyOrder

# Create the form class.
class CompanyOrderForm(ModelForm):
     class Meta:
        model = CompanyOrder
        fields = ['country', 'city', 'address', 'workers_number', 'start_date', 'end_date']