# flake8: noqa
# type: ignore

from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.mixins import NameValidationMixin
from django.contrib.auth import password_validation


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

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Por favor, insira pelo menos 2 caracteres.',
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Por favor, insira pelo menos 2 caracteres.',
        }
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use a mesma senha digitada acima.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não coincidem', code='invalid')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Este e-mail já está sendo utilizado por outro usuário', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1

class RegisterForm(NameValidationMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
            )
    
    def save(self, commit= True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        
        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas não coincidem', code='invalid')
                )
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        
        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error('email', ValidationError(
                        'Este e-mail já está sendo utilizado por outro usuário',
                        code='unique'
                ))

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
