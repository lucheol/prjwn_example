from django.urls import reverse

from proj.menu_core import BASE_MENU, MenuObject

MENUS = BASE_MENU + [

    MenuObject(order=10, slug='suppliers.*', title="Suppliers", url=reverse("suppliers-index")),
    MenuObject(order=1001, slug='suppliers.config.*', title="Config", icon='fa-building'),
    MenuObject(order=100101, slug='suppliers.config.supplier', title="Suppliers", url=reverse("supplier-list")),
    MenuObject(order=100102, slug='suppliers.config.product', title="Products", url=reverse("product-list")),

]
