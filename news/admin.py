from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News

class NewsAdmin(SummernoteModelAdmin):  
    exclude = ('slug',)
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title','slug')
    summernote_fields = ('content', 'content_de', 'content_en', 'content_bg')

admin.site.register(News, NewsAdmin)