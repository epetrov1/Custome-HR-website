from modeltranslation.translator import translator, TranslationOptions
from .models import Category, SubCategory, Cv

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_fields = ('de', 'en', 'bg')

translator.register(Category, CategoryTranslationOptions)



class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_fields = ('de', 'en', 'bg')

translator.register(SubCategory, SubCategoryTranslationOptions)

