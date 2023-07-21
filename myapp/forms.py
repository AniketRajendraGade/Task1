from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Task

class user(forms.ModelForm):
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['DOB']
        t=timezone.now().date()
        d=date_of_birth
        age = (t - d).days // 365
        if age > 18:
            raise forms.ValidationError("age should be greater than 18!!")
        return DOB

    class Meta:
        model = Task    
        fields = ['name', 'email', 'pno', 'DOB']