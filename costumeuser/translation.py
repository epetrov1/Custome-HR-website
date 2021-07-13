""" from modeltranslation.translator import translator, TranslationOptions
from .models import Worker, Company

class WorkerTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'phone')
    required_fields = ('de', 'en', 'bg')

translator.register(Worker, WorkerTranslationOptions)



class CompanyTranslationOptions(TranslationOptions):
    fields = ('company_name', 'address', 'phone')
    required_fields = ('de', 'en', 'bg')

translator.register(Company, CompanyTranslationOptions) """