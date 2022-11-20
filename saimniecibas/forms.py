from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Saimnieciba


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Saimnieciba
        fields = '__all__'
        # exclude = ['user']

        # fields = ['name', 'email', 'username', 'location',
        #           'bio', 'short_intro', 'profile_image', 'social_github', 'social_linkedin', 'social_twitter', 'social_youtube', 'social_website']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
