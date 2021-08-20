from django_tables2 import columns

from suppliers.models import Supplier, Product
from switchblade_dashboard import tables as dashboard_table


class SupplierTable(dashboard_table.Table):

    class Meta(dashboard_table.Table.Meta):
        model = Supplier
        fields = ['name', 'active', 'created_on']
        exclude = ('select_row', )


class ProductTable(dashboard_table.Table):

    class Meta(dashboard_table.Table.Meta):
        model = Product
        fields = ['name', 'supplier', 'created_on' ]
        exclude = ('select_row', )
