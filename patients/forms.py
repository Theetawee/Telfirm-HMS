from django import forms

from patients.models import Patient, Test
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
            'tests'
        ]

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tests = forms.ModelMultipleChoiceField(
        queryset=Test.objects.all(),  # Provide the queryset of available tests
        widget=forms.CheckboxSelectMultiple,  # Use CheckboxSelectMultiple for multiple selections
        required=False,  # Set to True if it's required
    )


