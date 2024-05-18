from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserModel(AbstractUser):
    pass

class ServiceOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Service Option"
        verbose_name_plural = "Service Options"
    
class DetailsOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Details Option"
        verbose_name_plural = "Details Options"
    
class StandartOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Standard Option"
        verbose_name_plural = "Standard Options"

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.ForeignKey(ServiceOption, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
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
    
    class Meta: 
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-id']