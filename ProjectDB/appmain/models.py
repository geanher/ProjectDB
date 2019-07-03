# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bancos(models.Model):
    idbanco = models.ForeignKey('DetBancos', models.DO_NOTHING, db_column='idbanco')
    ci = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancos'
        unique_together = (('ci', 'idbanco'),)


class Clientes(models.Model):
    ci = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    apellido = models.CharField(max_length=40, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    deudor = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Correos(models.Model):
    idcorreo = models.ForeignKey('DetCorreos', models.DO_NOTHING, db_column='idcorreo')
    ci = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correos'
        unique_together = (('ci', 'idcorreo'),)


class DetBancos(models.Model):
    ci = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ci', primary_key=True)
    idbanco = models.IntegerField()
    tipo_cuenta = models.CharField(max_length=1, blank=True, null=True)
    n_cuenta = models.CharField(max_length=20, blank=True, null=True)
    n_tarjeta = models.CharField(max_length=20, blank=True, null=True)
    cod_seg = models.SmallIntegerField(blank=True, null=True)
    fecha_vencimiento = models.CharField(max_length=20, blank=True, null=True)
    usuario_internet = models.CharField(max_length=20, blank=True, null=True)
    clave_internet = models.CharField(max_length=20, blank=True, null=True)
    clave_cajero = models.SmallIntegerField(blank=True, null=True)
    num_telefono = models.CharField(max_length=20, blank=True, null=True)
    clave_especial = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_bancos'
        unique_together = (('ci', 'idbanco'),)


class DetCorreos(models.Model):
    idcorreo = models.IntegerField()
    ci = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ci', primary_key=True)
    ususario = models.CharField(max_length=20, blank=True, null=True)
    clave = models.CharField(max_length=20, blank=True, null=True)
    tlf_correo = models.CharField(max_length=20, blank=True, null=True)
    correo_rec = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_correos'
        unique_together = (('ci', 'idcorreo'),)


class DetFact(models.Model):
    num_factura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='num_factura', primary_key=True)
    cod_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='cod_producto')
    cantidad = models.SmallIntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    detalles = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_fact'
        unique_together = (('num_factura', 'cod_producto'),)


class Facturas(models.Model):
    num_factura = models.AutoField(primary_key=True)
    ci = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ci', blank=True, null=True)
    fecha_fact = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'


class MetPago(models.Model):
    num_factura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='num_factura', primary_key=True)
    tipo_pago = models.CharField(max_length=1)
    monto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'met_pago'
        unique_together = (('num_factura', 'tipo_pago'),)


class Preguntas(models.Model):
    idbanco = models.ForeignKey(DetBancos, models.DO_NOTHING, db_column='idbanco')
    ci = models.CharField(max_length=30)
    idpregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=40, blank=True, null=True)
    respuesta = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preguntas'
        unique_together = (('ci', 'idbanco', 'idpregunta'),)


class Productos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    tipo_prod = models.ForeignKey('TiposProductos', models.DO_NOTHING, db_column='tipo_prod', blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class TiposProductos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_productos'
