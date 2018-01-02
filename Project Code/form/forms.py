import re
from django import forms
from .models import Feedback, Login, Contact, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('firstname', 'lastname', 'email', 'suggestions')


class RegistrationForm(UserCreationForm):
    #username = forms.CharField(max_length=50, help_text="Enter username")
    #email = forms.EmailField(max_length=254, help_text="Enter email address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'state', 'subject')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subject', 'username', 'text')
