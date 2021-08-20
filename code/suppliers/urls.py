from django.contrib.auth.decorators import login_required
from django.urls import path, include

from suppliers.autocomplete import SupplierAutocomplete
from suppliers.views import SupplierList, SupplierCreate, SupplierDetail, SupplierUpdate, \
    SupplierDelete, ProductList, ProductCreate, ProductDetail, ProductUpdate, \
    ProductDelete
from switchblade_dashboard.decorators import register_resource

from switchblade_dashboard.views import DashboardIndexView

urlpatterns = [
    path('', include([
        path('', register_resource(DashboardIndexView.as_view(page_title='Suppliers', header='Suppliers', columns=[3, 3, 3, 3])), name='suppliers-index'),
    ])),

    path('suppliers/', include([
        path('', register_resource(SupplierList), name='supplier-list'),
        path('create/', register_resource(SupplierCreate), name='supplier-create'),
        path('detail/<int:pk>', register_resource(SupplierDetail), name='supplier-detail'),
        path('update/<int:pk>', register_resource(SupplierUpdate), name='supplier-update'),
        path('delete/<int:pk>', register_resource(SupplierDelete), name='supplier-delete'),
        path('autocomplete/', login_required(SupplierAutocomplete.as_view()), name='supplier-autocomplete'),
    ])),

    path('products/', include([
        path('', register_resource(ProductList), name='product-list'),
        path('create/', register_resource(ProductCreate), name='product-create'),
        path('detail/<int:pk>', register_resource(ProductDetail), name='product-detail'),
        path('update/<int:pk>', register_resource(ProductUpdate), name='product-update'),
        path('delete/<int:pk>', register_resource(ProductDelete), name='product-delete'),
    ])),




]
