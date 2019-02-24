"""passbook administration forms"""
from django import forms

from passbook.core.models import DummyFactor, PasswordFactor

GENERAL_FIELDS = ['name', 'slug', 'order', 'policies', 'enabled']

class PasswordFactorForm(forms.ModelForm):
    """Form to create/edit Password Factors"""

    class Meta:

        model = PasswordFactor
        fields = GENERAL_FIELDS + ['backends']
        widgets = {
            'name': forms.TextInput(),
            'order': forms.NumberInput(),
        }

class DummyFactorForm(forms.ModelForm):
    """Form to create/edit Dummy Factor"""

    class Meta:

        model = DummyFactor
        fields = GENERAL_FIELDS
        widgets = {
            'name': forms.TextInput(),
            'order': forms.NumberInput(),
        }
