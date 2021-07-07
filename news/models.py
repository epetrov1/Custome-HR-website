
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_create = models.DateField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = News.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = News.objects.all().filter(slug__iexact=slug).count()
        self.slug = slug

        if self.featured:
            try:
                temp = News.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except News.DoesNotExist:
                pass
        super(News, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title