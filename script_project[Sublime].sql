CREATE TABLE clientes(
	ci varchar(30) PRIMARY KEY,
	nombre varchar(40),
	apellido varchar(40),
	telefono varchar(20),
	direccion varchar(80),
	fecha_nac date,
	genero char(1),
	deudor bit, 
	monto int);


CREATE TABLE bancos(
	idbanco serial PRIMARY KEY,
	nombre varchar(30),
	website varchar(30)
	);

CREATE TABLE correos (
	idcorreo serial PRIMARY KEY,
	nombre varchar(30),
	website varchar(30)
	);

CREATE TABLE tipos_productos(
	idproducto serial PRIMARY KEY,
	nombre varchar(40)
	);
	
CREATE TABLE det_bancos (
	ci varchar(30),
	idbanco int,
	tipo_cuenta char,
	n_cuenta varchar(20),
	n_tarjeta varchar(20),
	cod_seg smallint,
	fecha_vencimiento varchar(20),
	usuario_internet varchar(20),
	clave_internet varchar(20),
	clave_cajero smallint, 
	num_telefono varchar(20),
	clave_especial varchar(20),
	CONSTRAINT det_bank_PK PRIMARY KEY (ci, idbanco),
	CONSTRAINT det_bank_FK FOREIGN KEY (ci) REFERENCES clientes(ci),
	CONSTRAINT det_bank2_fk FOREIGN KEY (idbanco) REFERENCES bancos(idbanco)
	ON DELETE CASCADE 
	ON UPDATE CASCADE
	);

CREATE TABLE preguntas(
	idbanco int,
	ci varchar(30),
	idpregunta serial PRIMARY KEY,
	pregunta varchar(40),
	respuesta varchar (40), 
	CONSTRAINT preguntas_FK FOREIGN KEY (ci, idbanco) REFERENCES det_bancos(ci, idbanco)
	);

CREATE TABLE det_correos(
	idcorreo int,
	ci varchar(30),
	ususario varchar(20),
	clave varchar(20),
	tlf_correo varchar(20),
	correo_rec varchar(20),
	CONSTRAINT det_correo_PK PRIMARY KEY (ci, idcorreo),
	CONSTRAINT det_correos_FK FOREIGN KEY (ci) REFERENCES clientes(ci),
	CONSTRAINT det_correos2_Fk FOREIGN KEY (idcorreo) REFERENCES correos(idcorreo)
	ON DELETE CASCADE
	ON UPDATE CASCADE
	);




CREATE TABLE facturas(
	num_factura serial PRIMARY KEY,
	ci varchar(20),
	fecha_fact timestamp,
	CONSTRAINT facturas_FK FOREIGN KEY (ci) REFERENCES clientes(ci)
	ON DELETE CASCADE
	ON UPDATE CASCADE
	);

CREATE TABLE met_pago(
	num_factura int,
	tipo_pago char,
	monto int,
	CONSTRAINT met_pago_PK PRIMARY KEY (num_factura, tipo_pago),
	CONSTRAINT met_pago_FK FOREIGN KEY (num_factura) REFERENCES facturas(num_factura)
	ON DELETE CASCADE
	ON UPDATE CASCADE
	);





CREATE TABLE productos (
	codigo serial PRIMARY KEY,
	nombre varchar(40),
	tipo_prod int,
	precio int,
	CONSTRAINT productos_FK FOREIGN KEY(tipo_prod) REFERENCES tipos_productos(idproducto)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
	);

CREATE TABLE det_fact(
	num_factura int,
	cod_producto int,
	cantidad smallint,
	precio int,
	detalles varchar(100),
	CONSTRAINT det_fact_PK PRIMARY KEY (num_factura, cod_producto),
	CONSTRAINT det_fact_FK FOREIGN KEY(num_factura) REFERENCES facturas(num_factura),
	CONSTRAINT det_fact_FK2 FOREIGN KEY (cod_producto) REFERENCES productos(codigo)
	ON DELETE CASCADE
	ON UPDATE CASCADE
 	);


