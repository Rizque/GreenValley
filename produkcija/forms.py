from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['saimnieciba', 'p_datums']
        labels = {
            'p_nosaukums': 'Produkta nosaukums:',
            'p_apraksts': 'Apraksts:',
            'p_foto': 'Fotogrāfija:',
            'cena': 'Cena (EUR):',
            'cenas_mervieniba': 'Cenas mērvienība:',
            'termins': 'Realizācijas termiņš:',

        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})