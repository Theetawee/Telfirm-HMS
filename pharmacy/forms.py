from django import forms
from .models import Prescription
from .models import Drug  # Import the Drug model

class DrugForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['drugs']
        widgets = {
            'drugs': forms.CheckboxSelectMultiple(attrs={'class': 'drug-checkbox'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(DrugForm, self).__init__(*args, **kwargs)
        self.fields['drugs'].required = True  # Set the 'name' field as required