from django.contrib import admin
from .models import Produto, Compras, Cliente

admin.site.register(Produto)
admin.site.register(Compras)
admin.site.register(Cliente)