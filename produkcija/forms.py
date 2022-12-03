from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['title', 'featured_image', 'description',
        #           'demo_link', 'source_link', 'tags']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'Add title'})
