from django import forms
from .models import Prescription
from .models import Drug  # Import the Drug model

class DrugForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['drugs', 'detail']
        widgets = {
            'drugs': forms.CheckboxSelectMultiple(attrs={'class': 'drug-checkbox'}),
        }
