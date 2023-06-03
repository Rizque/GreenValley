from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Farm, Client
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Lietotājvārds'
        self.fields['email'].label = 'E-pasts'
        self.fields['password1'].label = 'Parole'
        self.fields['password2'].label = 'Parole vēlreiz'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'date', 'username']

        labels = {
            'first_name': 'Vārds:',
            'last_name': 'Uzvārds:',
            'foto': 'Fotogrāfija:',    
            'email': 'E-pasts:',
            'phone': 'Tālrunis:',
        }


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class FarmForm(ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'
        exclude = ['owner', 'date', 'longitude', 'latitude']

        labels = {
            'name': 'Saimniecības nosaukums:',
            'description': 'Apraksts:',
            'foto': 'Fotogrāfija:',
            'phone': 'Tālrunis:',
            'country': 'Valsts:',
            'city': 'Pilsēta:',
            'address': 'Adrese:',
        }


    def __init__(self, *args, **kwargs):
        super(FarmForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

