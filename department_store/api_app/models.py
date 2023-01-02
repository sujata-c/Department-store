from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    description = models.TextField()
    class Meta:
        managed = True
        db_table ='category'

class Items(models.Model):
    ''' Always use DecimalField for money. Even simple
    operations (addition, subtraction) are not immune to float rounding issues'''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30,null=True)
    description = models.TextField(default='')
    marked_rate =models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table ='items'


class Suppliers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, default='abc')
    address = models.TextField()
    contact = models.CharField(max_length=10)
    class Meta:
        managed=True
        db_table = 'suppliers'

    def __str__(self):
        return self.name


class Item_Sup(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    sup_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)

    class Meta:
        managed= True
        db_table='item_supplier'

class Metadata:
    pass



