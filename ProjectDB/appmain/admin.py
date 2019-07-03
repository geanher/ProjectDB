from django.contrib import admin

from appmain.models import Bancos, Clientes, Correos, DetBancos, DetCorreos, DetFact, Facturas, MetPago, Preguntas, Productos, TiposProductos

admin.site.register(Bancos)
admin.site.register(Clientes)
admin.site.register(Correos)
admin.site.register(DetBancos)
admin.site.register(DetCorreos)
admin.site.register(DetFact)
admin.site.register(Facturas)
admin.site.register(MetPago)
admin.site.register(Preguntas)
admin.site.register(Productos)
admin.site.register(TiposProductos)


# Register your models here.
