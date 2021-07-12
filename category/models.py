from django.db import models
from django.urls import reverse
from costumeuser.models import Company, Worker, User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name= models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:category_list', kwargs={'id': self.category.id, 'id': self.category_1.id})

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", related_query_name="category", verbose_name="category")
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="category_pic")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:company_order', kwargs={'id': self.subcategory.id})


class Cv(models.Model):
    GENDER = [
        ('Femail', _('Femail')),
        ('Male', _('Male')),
    ]

    DRIVING_LICENSE = [
        ('Yes', _('Yes')),
        ('No', _('No')),
    ]
    LANG1 = [
        ('English', _('English')),
        ('German', _('German')),
        ('French', _('French')),
        ('Italian', _('Italian')),
        ('Spanish', _('Spanish')),
        ('Russian', _('Russian')),
    ]

    LANG_LEVELS = [
        ('Basic', _('Basic')),
        ('Medium', _('Medium')),
        ('Fluent', _('Fluent')),
    ]

    COUNTRY = [
        ('UK', _('UK')),
        ('Germany', _('Germany')),
        ('France', _('France')),
        ('Italy', _('Italy')),
        ('Netherlands', _('Netherlands')),
        ('Switzerland', _('Switzerland')),
        ('Poland', _('Poland')),
        ('Greece', _('Greece')),
        ('Sweden', _('Sweden')),
        ('Bulgaria', _('Bulgaria')),
        ('Belgium', _('Belgium')),
        ('Austria', _('Austria')),
        ('Hungary', _('Hungary')),
        ('Denmark', _('Denmark')),
        ('Finland', _('Finland')),
        ('Norway', _('Norway')),
        ('Czechia', _('Czechia')),
        ('Irland', _('Irland')),
        ('Romania', _('Romania')),
        ('Cyprus', _('Cyprus')),
        ('Slovenia', _('Slovenia')),
        ('Lithuania', _('Lithuania')),
        ('Latvia', _('Latvia')),
        ('Russian Federation', _('Russian Federation')),
        ('Not Europe', _('Not Europe')),
    ]

    POSITION = [
        ('Position I aplly', _('Position I apply')),
        ('Different', _('Different')),
    ]

    job = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_day = models.DateField(_("birth_day"))
    gender = models.CharField(_('gender'), max_length=50, choices=GENDER)
    driving_license = models.CharField(_('driving_license'), max_length=10, choices=DRIVING_LICENSE)
    first_lang = models.CharField(_('first_lang'), max_length=20, choices=LANG1, blank=True)
    first_lang_level = models.CharField(_("first_lang_level"), max_length=50, choices=LANG_LEVELS, blank=True)
    second_lang = models.CharField(_('second_lang'), max_length=20, choices=LANG1, blank=True)
    second_lang_level = models.CharField(_("second_lang_level"), max_length=50, choices=LANG_LEVELS, blank=True)
    third_lang = models.CharField(_('third_lang'), max_length=20, choices=LANG1, blank=True)
    third_lang_level = models.CharField(_('third_lang_level'), max_length=50, choices=LANG_LEVELS, blank=True)
    ready_to_start = models.DateField(_('ready_to_start'),)
    expectet_salary = models.CharField(_('expectet_salary'), max_length=20, blank=True)
    sertificate_1 = models.ImageField(_("sertificate_1"), upload_to="cv_sertificate", blank=True)
    sertificate_2 = models.ImageField(_("sertificate_2"), upload_to="cv_sertificate", blank=True)

    #Last 3 job Expiriance 
    country_1 = models.CharField(_('country_1'), max_length=50, choices=COUNTRY) #help_text=_('Country you worked'))
    company_name_1 = models.CharField(_('company_name_1'), max_length=50)
    position_1 = models.CharField(_("position_1"), max_length=150, choices=POSITION, default="Position I aplly")
    start_date_1 = models.DateField(_('start_date_1'),)
    end_date_1 = models.DateField(_('end_date_1'),)
    country_2 = models.CharField(_('country_2'), max_length=50, choices=COUNTRY)
    company_name_2 = models.CharField(_('company_name_2'), max_length=50)
    position_2 = models.CharField(_('position_2'), max_length=150, choices=POSITION, default="Position I aplly")
    start_date_2 = models.DateField(_('start_date_2'),)
    end_date_2 = models.DateField(_('end_date_2'),)
    country_3 = models.CharField(_('country_3'), max_length=50, choices=COUNTRY)
    company_name_3 = models.CharField(_('company_name_3'), max_length=50)
    position_3 = models.CharField(_('position_3'), max_length=150, choices=POSITION, default="Position I aplly")
    start_date_3 = models.DateField(_('start_date_3'),)
    end_date_3 = models.DateField(_('end_date_3'),)

    update_date = models.DateTimeField(auto_now=True)
    submit_date = models.DateField(auto_now_add=True)
    employ = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('category:cv_detail', kwargs={'id': self.cv.id})


class CompanyOrder(models.Model):
    job_titlle = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subcategory")
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(_('country'), max_length=100)
    city = models.CharField(_('city'), max_length=100)
    address = models.CharField(_('address_order'), max_length=250)
    workers_number = models.CharField(_('workers_number'), max_length=10)
    start_date = models.DateField(_('start_date'),)
    end_date = models.DateField(_('end_date'),)
    update_date = models.DateTimeField(auto_now=True)
    submit_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('category:order_detail', kwargs={'id': self.companyorder.id})
