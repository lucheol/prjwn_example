from django.urls import reverse_lazy

from suppliers.filters import SupplierFilter, ProductFilter
from suppliers.forms import SupplierForm, ProductForm
from suppliers.models import Supplier, Product
from suppliers.tables import SupplierTable, ProductTable
from switchblade_dashboard.views import DashboardListView, DashboardDeleteView, DashboardUpdateView, DashboardCreateView, \
    DashboardDetailView


class SupplierList(DashboardListView):

    page_title = 'Supplier'
    header = 'Supplier list'

    add_button_title = 'New supplier'
    add_button_url = reverse_lazy('supplier-create')

    table_class = SupplierTable
    filter_class = SupplierFilter
    object = Supplier

    def get_queryset(self):
        qs = Supplier.objects.filter()
        return qs


class SupplierDetail(DashboardDetailView):

    page_title = 'Supplier'
    header = 'Supplier detail'
    object = Supplier

    rows_based_on_form = SupplierForm

    def get_queryset(self):
        qs = Supplier.objects.filter()
        return qs


class SupplierCreate(DashboardCreateView):

    page_title = 'Supplier'
    header = 'Add supplier'

    form_class = SupplierForm
    object = Supplier

    show_button_save_continue = True
    owner_include = True

    success_message = 'Supplier created successfully.'

    success_redirect = 'supplier-list'


class SupplierUpdate(DashboardUpdateView):

    page_title = 'Supplier'
    header = 'Edit supplier'

    form_class = SupplierForm
    object = Supplier

    success_message = 'Supplier updated successfully.'
    success_redirect = 'supplier-list'

    def get_queryset(self):
        qs = Supplier.objects.filter()
        return qs


class SupplierDelete(DashboardDeleteView):

    success_message = 'Supplier deleted successfully.'
    success_redirect = 'supplier-list'

    header = 'Delete supplier'

    object = Supplier
    validate_owner = False

    def get_queryset(self):
        qs = Supplier.objects.filter()
        return qs


class ProductList(DashboardListView):

    page_title = 'Products'
    header = 'Product list'

    add_button_title = 'New product'
    add_button_url = reverse_lazy('product-create')

    table_class = ProductTable
    filter_class = ProductFilter
    object = Product

    def get_queryset(self):
        qs = Product.objects.filter()
        return qs


class ProductDetail(DashboardDetailView):

    page_title = 'Products'
    header = 'Product detail'
    object = Product

    rows_based_on_form = ProductForm

    def get_queryset(self):
        qs = Product.objects.filter()
        return qs


class ProductCreate(DashboardCreateView):

    page_title = 'Products'
    header = 'Add product'

    form_class = ProductForm
    object = Product

    show_button_save_continue = True
    owner_include = True

    success_message = 'Product created successfully.'

    success_redirect = 'product-list'


class ProductUpdate(DashboardUpdateView):

    page_title = 'Products'
    header = 'Edit product'

    form_class = ProductForm
    object = Product

    success_message = 'Product updated successfully.'
    success_redirect = 'product-list'

    def get_queryset(self):
        qs = Product.objects.filter()
        return qs


class ProductDelete(DashboardDeleteView):

    success_message = 'Product deleted successfully.'
    success_redirect = 'product-list'

    header = 'Delete product'

    object = Product
    validate_owner = False

    def get_queryset(self):
        qs = Product.objects.filter()
        return qs



