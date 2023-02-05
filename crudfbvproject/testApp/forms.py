from django import forms
from testApp.models import EmployeeForm

class EmployeeForm1(forms.ModelForm):
    class Meta:
        model = EmployeeForm
        fields = '__all__'

