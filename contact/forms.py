# flake8: noqa
# type: ignore

from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category',)

        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'phone': 'Celular',
            'email': 'E-mail',
            'description': 'Descrição',
            'category': 'Categoria',
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
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name:
            if first_name.strip().lower() == last_name.strip().lower():
                self.add_error('last_name', ValidationError(
                    'O último nome não pode ser igual ao primeiro nome.',
                    code='invalid'
                ))

        return cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise ValidationError(
                'O campo "Primeiro nome" é obrigatório.',
                code='required'
            )

        if len(first_name.strip()) < 2:
            raise ValidationError(
                'O primeiro nome deve ter pelo menos 2 caracteres.',
                code='invalid'
            )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise ValidationError(
                'O campo "Último nome" é obrigatório.',
                code='required'
            )

        return last_name

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

        if not '@' in email:
            raise ValidationError('Informe um e-mail válido.', code='invalid')

        return email
