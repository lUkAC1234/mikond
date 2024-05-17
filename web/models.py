from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserModel(AbstractUser):
    pass

class ServiceOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class DetailsOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class StandartOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class ServiceModel(models.Model):
    title = models.CharField(max_length=100)
    options = models.ManyToManyField(DetailsOption)
    standard_equipment = models.ManyToManyField(StandartOption)
    service = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)
    short_detail = models.CharField(max_length=300)
    detail = models.TextField()
    image = models.ImageField(upload_to='service/images/%Y/%m/%d/')

    def __str__(self):
        return self.title