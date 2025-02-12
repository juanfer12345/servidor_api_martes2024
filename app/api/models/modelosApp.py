from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

#GASTO
class Gasto(Base):
    #id
    #monto
    #fecha
    #descripcion
    #nombre
    pass

#CATEGORIA
class Categoria(Base):
    pass
    #id
    #nombreCategoria
    #descripcion
    #fotoicono

#METODOS DE PAGO
class MetodoPago(Base):
    pass
    #id
    #nombreMetodo
    #descripcion

#FACTURA
class Factura(Base):
    pass