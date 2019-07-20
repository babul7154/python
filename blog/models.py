from django.db import models

# Create your models here.
class BookInfo(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_yr=models.DateField()
    rating=models.IntegerField()
class uread(models.Model):
    uread_rating=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    publisher=models.CharField(max_length=200)