from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Faq

class FaqAdmin(SummernoteModelAdmin):  
    exclude = ('slug',)
    list_display = ('id', 'question', 'slug')
    list_display_links = ('question','slug')
    summernote_fields = ('answer', 'answer_de', 'answer_en', 'answer_bg')

admin.site.register(Faq, FaqAdmin)