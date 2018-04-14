from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.Profile
        fields = UserCreationForm.Meta.fields + ('about',)

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = models.User
#         fields = ('name', 'userid', 'password',  'about')

class RatingForm(forms.ModelForm):
    # if user1.canRate = 1 and edit if canEdit = 1
    class Meta:
        model = models.Rating
        fields = ('user1', 'user2', 'rating')

class WorkForm(forms.ModelForm):
    class Meta:
        model = models.Work
        fields = ('user', 'work')

class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('username', 'password')