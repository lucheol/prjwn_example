import django_filters
from suppliers.models import Supplier, Product
from dal import autocomplete


class SupplierFilter(django_filters.FilterSet):

    class Meta:
        model = Supplier
        fields = {
            'name': ['icontains'],
            'active': ['exact']
        }


class ProductFilter(django_filters.FilterSet):

    supplier = django_filters.ModelMultipleChoiceFilter(queryset=Supplier.objects.all(),
                                                       field_name='supplier',
                                                       widget=autocomplete.ModelSelect2Multiple(
                                                         url='supplier-autocomplete',
                                                       )
                                                     )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'supplier': ['exact']
        }
