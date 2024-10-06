from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=50,null=True)
    Mobile=models.CharField(max_length=15,null=True)
    Message=models.TextField(null=True)

class category(models.Model):
    category_name=models.CharField(max_length=100,null=True)
    category_picture=models.ImageField(upload_to='static/category/',null=True)
    def __str__(self):
        return self.category_name

class slider(models.Model):
    slider_picture=models.ImageField(upload_to='static/slider/',null=True)
    slider_title=models.CharField(max_length=50,null=True)
    slider_description=models.TextField(null=True)

class tbl_jobs(models.Model):
    title=models.CharField(max_length=50,null=True)
    title_link=models.CharField(max_length=100,null=True)
    posted_date=models.DateField(null=True)

class tbl_city(models.Model):
    city_name=models.CharField(max_length=50,null=True)
    city_picture=models.ImageField(upload_to='static/city/',null=True)
    def __str__(self):
        return self.city_name

class tbl_news(models.Model):
    headline=models.CharField(max_length=400,null=True)
    news_category=models.ForeignKey(category,on_delete=models.CASCADE)
    news_city=models.ForeignKey(tbl_city,on_delete=models.CASCADE)
    news_description=models.TextField(null=True)
    posted_date=models.DateField(null=True)
    news_picture=models.ImageField(upload_to='static/news/',null=True)

class video_news(models.Model):
    news_headline=models.CharField(max_length=400,null=True)
    news_description=HTMLField(null=True)
    posted_date=models.DateField(null=True)
    video_link=models.CharField(max_length=100,null=True)
