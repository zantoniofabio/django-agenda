from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "classe-a classe-b",
                    "placeholder": "Seu primeiro nome",
                }
            )
        }

    def clean(self):  # manipula antes de salvar
        # cleaned_data = self.cleaned_data

        self.add_error(
            "first_name", ValidationError("Mensagem de erro", code="invalid")
        )
        self.add_error(
            "first_name", ValidationError("Mensagem de erro 2", code="invalid")
        )

        return super().clean()
