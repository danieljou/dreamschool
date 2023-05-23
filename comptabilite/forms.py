from django import forms
from .models import *

from django.forms import (
    CheckboxInput,TextInput,ModelForm,EmailInput, 
    NumberInput, DateInput, 
    BooleanField, Select, FileInput,
    Textarea,
    
)


class EcheancePaiementForm(forms.ModelForm):
    
    class Meta:
        model = EcheancePaiement
        exclude = ('session', )
        widgets = {
             'date_debut' : TextInput(
                attrs = {
                   
                    'type':"date"
                }
            ),
            'date_fin' : TextInput(
                attrs = {
                   
                    'type':"date"
                }
            ),
        }


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        exclude = ('date_paiement',)
