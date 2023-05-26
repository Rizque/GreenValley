from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['farm', 'date']
        labels = {
            'name': 'Produkta nosaukums:',
            'description': 'Apraksts:',
            'foto': 'Fotogrāfija:',
            'price': 'Cena (EUR):',
            'unit': 'Cenas mērvienība:',
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
