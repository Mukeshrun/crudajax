from django import forms
from . models import User
class UserRegistertion(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'password'})
        }