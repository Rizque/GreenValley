from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # labels = {
        #     'first_name': 'Name',
        # }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'username', 's_datums']
        labels = {
            's_nosaukums': 'Saimniecības nosaukums:',
            's_apraksts': 'Apraksts:',
            's_foto': 'Fotogrāfija:',
            'email': 'Epasts:',
            'talrunis': 'Tālrunis:',
            'lokacija': 'Lokācija:',
        }

        # fields = ['name', 'email', 'username', 'location',
        #           'bio', 'short_intro', 'profile_image', 'social_github', 'social_linkedin', 'social_twitter', 'social_youtube', 'social_website']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
