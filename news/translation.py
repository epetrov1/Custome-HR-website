from modeltranslation.translator import translator, TranslationOptions
from .models import News

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title','content')
    required_fields = ('de', 'en', 'bg')

translator.register(News, BlogPostTranslationOptions)