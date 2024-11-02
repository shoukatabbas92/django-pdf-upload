from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PDF
from django import forms


class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['title', 'file']


class UserRegistrationForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email', "password1", "password2"]