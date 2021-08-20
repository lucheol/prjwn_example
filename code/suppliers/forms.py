from crispy_forms.layout import Layout, Fieldset, Column
from dal import autocomplete, forward
from django import forms

from suppliers.models import Supplier, Product


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'
        exclude = ('created_by', 'created_on', 'modified_by', 'modified_on')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('created_by', 'created_on', 'modified_by', 'modified_on')
        widgets = {
            'supplier': autocomplete.ModelSelect2(url='supplier-autocomplete'),
        }
