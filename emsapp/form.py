from .models import Employee
from django import forms

class empform(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
    
