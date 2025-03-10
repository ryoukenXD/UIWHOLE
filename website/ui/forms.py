from django import forms
from .models import Employee  # Ensure the correct model is imported

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  # Make sure this matches the correct model
        fields = '__all__'  # OR list all fields manually
