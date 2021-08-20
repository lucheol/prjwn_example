from django.db import models

from switchblade_dashboard.models import DashboardBaseModel


class Supplier(DashboardBaseModel):
    name = models.CharField(max_length=80, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def dict_repr(self):
        return {
            'Name': self.name,
            'Active': self.active
        }

    @classmethod
    def _filter_by_str(cls, q, first_match_id=True, raise_when_not_found=True):
        return super()._filter_by_str({'name': q})


class Product(DashboardBaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, unique=True)
    in_stock = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def dict_repr(self):
        return {
            'Name': self.name,
            'Supplier': self.supplier.name,
            'In Stock': self.in_stock,
            'Active': self.active
        }

    @classmethod
    def _filter_by_str(cls, q, first_match_id=True, raise_when_not_found=True):
        return super()._filter_by_str({'name': q})

