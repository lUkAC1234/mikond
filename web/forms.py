from django import forms
from django.core.exceptions import ValidationError
from .models import ContactModel

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'service', 'message']
        error_messages = {
            'name': {'required': "Введите ваше имя"},
            'email': {'required': "Введите вашу почту"},
            'service': {'required': "Выберите нужный сервис"},
            'message': {'required': "Введите ваше сообщение"}
        }