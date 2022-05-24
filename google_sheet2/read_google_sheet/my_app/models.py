from django.db import models



"""
orders = Table('orders', metadata,
               Column('id', Integer(), primary_key=True),
               Column('order', Integer(), nullable=False),
               Column('prise_usd', Integer(), nullable=False),
               Column('delivery_time', Date()),
               Column('price_ru', Integer(), nullable=False),
               )
"""


class Orders(models.Model):
    order = models.IntegerField(unique=True)
    prise_usd = models.IntegerField()
    delivery_time = models.DateField()
    price_ru = models.IntegerField()
