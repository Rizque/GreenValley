from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Lietotājvārds:'
        self.fields['email'].label = 'E-pasts:'
        self.fields['password1'].label = 'Parole:'
        self.fields['password2'].label = 'Parole vēlreiz:'

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

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
