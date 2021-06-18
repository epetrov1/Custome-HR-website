from django.db import models
from costumeuser.models import Company, Worker

class Category(models.Model):
    name= models.CharField(max_length=250)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", related_query_name="category", verbose_name="category")
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="category_pic")

    def __str__(self):
        return self.name


""" class Cv(models.Model):
    job = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    worker = models.(Worker, on_delete=models.CASCADE)
    birth_day = models.Date()
    gender = models.CharField(max_length=50)
    driving_license = models.CharField(max_length=10)
    lang1 = models.CharField(max_length=20)
    lang1_level = models.CharField(max_length=50)
    lang2 = models.CharField(max_length=20)
    lang2_level = models.CharField(max_length=50)
    lang3 = models.CharField(max_length=20)
    lang3_level = models.CharField(max_length=50)
    ready_to_start = models.Date()
    sertificate1 = models.ImageField(upload_to="cv_sertificate")
    sertificate1 = models.ImageField(upload_to="cv_sertificate")

    country1 = models.CharField(max_length=50)
    company_name1 = models.CharField(max_length=50)
    start_date1 = models.DateField()
    end_date1 = models.DateField()
    country2 = models.CharField(max_length=50)
    company_name2 = models.CharField(max_length=50)
    start_date2 = models.DateField()
    end_date2 = models.DateField()
    country3 = models.CharField(max_length=50)
    company_name3 = models.CharField(max_length=50)
    start_date3 = models.DateField()
    end_date3 = models.DateField()
    employ = models.BooleanField(default=False) """


""" class CompanyOrder(models.Model):
    job_titlle = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    workers_number = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
 """