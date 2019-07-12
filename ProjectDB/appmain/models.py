from django.db import models

class Bancos(models.Model):
    idbanco = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancos'
    
    def __str__(self):
        return '{}'.format(self.nombre)


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

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Correos(models.Model):
    idcorreo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correos'

    def __str__(self):
        return '{}'.format(self.nombre)


class DetBancos(models.Model):
    #iddetbanco = models.AutoField()
    ci = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ci')
    idbanco = models.ForeignKey(Bancos, models.DO_NOTHING, db_column='idbanco', blank=True, null=True)
    tipo_cuenta = models.CharField(max_length=1, blank=True, null=True)
    n_cuenta = models.CharField(max_length=20,primary_key=True)
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

class DetCorreos(models.Model):
    iddetcorreos = models.AutoField(primary_key=True)
    idcorreo = models.ForeignKey(Correos, models.DO_NOTHING, db_column='idcorreo')
    ci = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ci')
    ususario = models.CharField(max_length=20, blank=True, null=True)
    clave = models.CharField(max_length=20, blank=True, null=True)
    tlf_correo = models.CharField(max_length=20, blank=True, null=True)
    correo_rec = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_correos'


class DetFact(models.Model):
    iddetfact = models.AutoField(primary_key=True)
    num_factura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='num_factura')
    cod_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='cod_producto')
    cantidad = models.SmallIntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    detalles = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_fact'


class Facturas(models.Model):
    num_factura = models.AutoField(primary_key=True)
    ci = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ci', blank=True, null=True)
    fecha_fact = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'


class MetPago(models.Model):
    id_met = models.AutoField(primary_key=True)
    num_factura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='num_factura')
    tipo_pago = models.CharField(max_length=1, )
    monto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'met_pago'

class Preguntas(models.Model):
    n_cuenta = models.ForeignKey(DetBancos, models.DO_NOTHING, db_column='n_cuenta')
    #ci = models.CharField(max_length=20, blank=True, null=True)
    idpregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=40, blank=True, null=True)
    respuesta = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preguntas'


class Productos(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    tipo_prod = models.ForeignKey('TiposProductos', models.DO_NOTHING, db_column='tipo_prod', blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'

    def __str__(self):
        return '{}'.format(self.nombre)


class TiposProductos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_productos'

    def __str__(self):
        return '{}'.format(self.nombre)
