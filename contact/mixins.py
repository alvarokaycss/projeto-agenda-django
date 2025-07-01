# flake8: noqa
# type: ignore

from django.core.exceptions import ValidationError


class NameValidationMixin():
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
