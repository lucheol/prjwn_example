from .urls_base import *

urlpatterns = urlpatterns + [
    path('', include('suppliers.urls')),
]