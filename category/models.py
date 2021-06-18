from django.db import models

""" class Category(models.Model):
    name= models.CharField(max_length=250)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="category_pic")

    def __str__(self):
        return self.name


class Cv(models.Model):
    job = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
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
    start_date1 = models.Date()
    end_date1 = models.Date()
    country2 = models.CharField(max_length=50)
    company_name2 = models.CharField(max_length=50)
    start_date2 = models.Date()
    end_date2 = models.Date()
    country3 = models.CharField(max_length=50)
    company_name3 = models.CharField(max_length=50)
    start_date3 = models.Date()
    end_date3 = models.Date() """