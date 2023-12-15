from django import forms
from .models import Notice

class CreateNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"