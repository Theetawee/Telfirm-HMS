from django import forms
from .models import Prescription
from .models import Drug  # Import the Drug model

class DrugForm(forms.ModelForm):
    # Modify the "drug" field to use CheckboxSelectMultiple widget
    drug = forms.ModelMultipleChoiceField(
        queryset=Drug.objects.all(),  # Provide the queryset of all drugs
        widget=forms.CheckboxSelectMultiple,  # Use CheckboxSelectMultiple widget
    )

    class Meta:
        model = Prescription
        fields = ['drug', 'detail']
