from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# --------------------------------------------------------------------------- #
# Users
class UserModel(AbstractUser):
    pass
# --------------------------------------------------------------------------- #

class CategoryModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Projects category'
        verbose_name_plural = 'Projects categories'

class ProjectsModel(models.Model):
    title = models.CharField(max_length=50)
    main_image = models.ImageField(upload_to='projects/main-image/%Y/%m/%d/')
    luster_image = models.ImageField(upload_to='projects/luster/%Y/%m/%d/')
    rotate_image = models.ImageField(upload_to='projects/rotate-image/%Y/%m/%d/')
    size_image = models.ImageField(upload_to='projects/size/%Y/%m/%d/')
    sizes = models.CharField(max_length=50)
    project_info = models.TextField(max_length=500)
    by = models.CharField(max_length=32)
    by_whom_text = models.TextField(max_length=500)
    categories = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'), related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ('-id',)


class CollectionsCategoryModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Collections category'
        verbose_name_plural = 'Collections categories'

class CollectionsModel(models.Model):
    title = models.CharField(max_length=50)
    main_image = models.ImageField(upload_to='collections/main-image/%Y/%m/%d/')
    luster_image = models.ImageField(upload_to='collections/luster/%Y/%m/%d/')
    rotate_image = models.ImageField(upload_to='collections/rotate-image/%Y/%m/%d/')
    size_image = models.ImageField(upload_to='collections/size/%Y/%m/%d/')
    sizes = models.CharField(max_length=50)
    project_info = models.TextField(max_length=500)
    by = models.CharField(max_length=32)
    by_whom_text = models.TextField(max_length=500)
    categories = models.ForeignKey(CollectionsCategoryModel, on_delete=models.CASCADE, verbose_name=_('category'), related_name='collection')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'collection'
        verbose_name_plural = 'collections'
        ordering = ('-id',)


class ContactUSModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    email = models.EmailField(max_length=45, verbose_name=_('email'))
    message = models.CharField(max_length=300, verbose_name=_('message'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_('user'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ('-id',)

class LogoModel(models.Model):
    logo = models.ImageField(upload_to='logos/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'
        ordering = ('-id',)