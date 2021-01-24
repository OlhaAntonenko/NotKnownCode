from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=150, default='NotKnown')
    price = models.FloatField(default=0.0)
    description = models.TextField(max_length=500, default='', blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.name}, id: {self.id}, active: {self.is_active}'
