from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required='true')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', ]


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required='true')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'instagram_url', 'bio']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField(required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
