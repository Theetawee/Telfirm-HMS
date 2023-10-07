from django import forms
from .models import Patient

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'contact_number',
            'address',
            'status',
            'ward',
            'allergies',
            'current_medications',
            'medical_conditions',
            'emergency_contact_name',
            'emergency_contact_number',
            'comments',
            'micro',
            'parasitology',
            'haematology',
            'chemistry',
            'immunology'
        ]

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    
