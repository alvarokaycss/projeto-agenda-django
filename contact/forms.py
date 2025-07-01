# flake8: noqa
# type: ignore

from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.mixins import NameValidationMixin


class ContactForm(NameValidationMixin, forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'picture', )

        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'phone': 'Celular',
            'email': 'E-mail',
            'description': 'Descrição',
            'category': 'Categoria',
            'picture': 'Imagem do contato',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ex: Maria'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ex: Silva'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Ex: (99) 99999-9999'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ex: maria@email.com'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descreva observações...'
            }),
            'picture': forms.FileInput(attrs={
                'accept': 'image/*'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            raise ValidationError('O campo "Celular" é obrigatório.', code='required')

        if len(phone) < 10:
            raise ValidationError('Número de celular inválido.', code='invalid')

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise ValidationError('O campo "E-mail" é obrigatório.', code='required')

        if '@' not in email:
            raise ValidationError('Informe um e-mail válido.', code='invalid')

        return email


class RegisterForm(NameValidationMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
            )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError(
                    'Este e-mail já está sendo utilizado por outro usuário',
                    code='unique'
            ))

        return email
