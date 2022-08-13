""" <!-- 
  pip install djangorestframework
  Verificar instalacion con pip list
  Crear un nuevo con django-admin startapp rest_producto
  Crear archivo serializers.py
  
 --> """


from rest_producto import serializers
from core.models import Producto

class ProductoSerializers(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = ['idProducto','nombreProducto', 'valorProducto', 'categoria']