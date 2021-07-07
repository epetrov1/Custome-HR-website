from modeltranslation.translator import translator, TranslationOptions
from .models import Faq

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('question','answer')
    required_fields = ('de', 'en', 'bg')

translator.register(Faq, BlogPostTranslationOptions)