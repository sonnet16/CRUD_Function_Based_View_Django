from django import forms
from .models import Users


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'passwordid'})
        }
