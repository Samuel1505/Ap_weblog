from django.db import models
from django.urls import reverse

# Create your models here.
# class blog(models.Model):
    # title = models.CharField(max_length=100)
    # author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    # body = models.TextField()
    
    # def __str__(self):
    #     return self.title
    # def get_absolute_url(self):
    #     return reverse("details", kwargs={"pk": self.pk})
    
    
class weblog(models.Model):
    Firstname = models.CharField(max_length=20)
    def __str__(self):
        return self.Firstname
    Lastname = models.CharField(max_length=20)
    
    Gender = models.CharField(max_length=20)
    
    
    Date_of_birth = models.DateField()
    
    email = models.EmailField()  
    
    phone_number = models.CharField(max_length=20)
    
    Matric_number = models.CharField(max_length=20)
    
    
    def get_absolute_url(self):
       return reverse("details", kwargs={"pk": self.pk})