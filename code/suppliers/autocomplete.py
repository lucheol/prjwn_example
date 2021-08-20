from dal import autocomplete
from suppliers.models import Supplier


class SupplierAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Supplier.objects.filter()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
