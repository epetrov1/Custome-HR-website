from django.db import models
from django.urls import reverse
from costumeuser.models import Company, Worker, User

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
        ('Femail', 'Femail'),
        ('Male', 'Male'),
    ]

    DRIVING_LICENSE = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    LANG1 = [
        ('English', 'English'),
        ('German', 'German'),
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('Spanish', 'Spanish'),
        ('Turkish', 'Turkish'),
        ('Russian', 'Russian'),
    ]

    LANG_LEVELS = [
        ('Basic', 'Basic'),
        ('Medium', 'Medium'),
        ('Fluent', 'Fluent'),
    ]

    COUNTRY = [
        ('UK', 'UK'),
        ('Germany', 'Germany'),
        ('France', 'France'),
        ('Italy', 'Italy'),
        ('Netherlands', 'Netherlands'),
        ('Switzerland', 'Switzerland'),
        ('Poland', 'Poland'),
        ('Greece', 'Greece'),
        ('Sweden', 'Sweden'),
        ('Bulgaria', 'Bulgaria'),
        ('Belgium', 'Belgium'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Denmark', 'Denmark'),
        ('Finland', 'Finland'),
        ('Norway', 'Norway'),
        ('Czechia', 'Czechia'),
        ('Irland', 'Irland'),
        ('Romania', 'Romania'),
        ('Cyprus', 'Cyprus'),
        ('Slovenia', 'Slovenia'),
        ('Lithuania', 'Lithuania'),
        ('Latvia', 'Latvia'),
        ('Russian Federation', 'Russian Federation'),
        ('Not Europe', 'Not Europe'),
    ]


    job = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_day = models.DateField()
    gender = models.CharField(max_length=50, choices=GENDER)
    driving_license = models.CharField(max_length=10, choices=DRIVING_LICENSE)
    first_lang = models.CharField(max_length=20, choices=LANG1, blank=True)
    first_lang_level = models.CharField(max_length=50, choices=LANG_LEVELS, blank=True)
    second_lang = models.CharField(max_length=20, choices=LANG1, blank=True)
    second_lang_level = models.CharField(max_length=50, choices=LANG_LEVELS, blank=True)
    third_lang = models.CharField(max_length=20, choices=LANG1, blank=True)
    third_lang_level = models.CharField(max_length=50, choices=LANG_LEVELS, blank=True)
    ready_to_start = models.DateField()
    expectet_salary = models.CharField(max_length=20, blank=True)
    sertificate_1 = models.ImageField(upload_to="cv_sertificate", blank=True)
    sertificate_2 = models.ImageField(upload_to="cv_sertificate", blank=True)

    #Last 3 job Expiriance 
    country_1 = models.CharField(max_length=50, choices=COUNTRY)
    company_name_1 = models.CharField(max_length=50)
    start_date_1 = models.DateField()
    end_date_1 = models.DateField()
    country_2 = models.CharField(max_length=50, choices=COUNTRY)
    company_name_2 = models.CharField(max_length=50)
    start_date_2 = models.DateField()
    end_date_2 = models.DateField()
    country_3 = models.CharField(max_length=50, choices=COUNTRY)
    company_name_3 = models.CharField(max_length=50)
    start_date_3 = models.DateField()
    end_date_3 = models.DateField()

    submit_date = models.DateField(auto_now_add=True)
    employ = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('category:cv_detail', kwargs={'id': self.cv.id})


class CompanyOrder(models.Model):
    job_titlle = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subcategory")
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    workers_number = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    submit_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('category:order_detail', kwargs={'id': self.companyorder.id})
