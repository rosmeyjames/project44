from django.db import models
# Create your models here .
class author(models.Model):
    authorname=models.CharField(max_length=200,null=True)
    def __str__(self):
          return '{}'.format(self.authorname)

class book(models.Model):
     bookname=models.CharField(max_length=200)
     bookauthor=models.ForeignKey(author,on_delete=models.CASCADE)
     bookprice=models.IntegerField()

     bookimage=models.ImageField(upload_to='book/')
     quantity=models.IntegerField()

     def __str__(self):
          return '{}'.format(self.bookname)
class userprofile(models.Model):
     username = models.CharField(max_length=200)
     email=models.EmailField
     first_name = models.CharField(max_length=200)
     last_name = models.CharField(max_length=200)
     password=models.CharField(max_length=200)
     confirmpassword=models.CharField(max_length=200)

class logintable(models.Model):
     username = models.CharField(max_length=200)
     password = models.CharField(max_length=200)
     usertype= models.CharField(max_length=200)