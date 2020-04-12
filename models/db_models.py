from components.db.connection import db,BaseModel
from peewee import *


class ListField(Field):
    def db_value(self, value):
        return ','.join(value)

    def python_value(self, value):
        return value.split(',')


class Reserva(BaseModel):
    idReserva = TextField(unique=True)
    idBienComun = TextField()
    idPropiedadHorizontal = TextField()
    numeroIdentificacion = TextField()
    tipoIdentificacion = TextField()
    fechaReserva = DateTimeField()
    horaInicio = TextField()
    horaFinal = TextField()
    # datetime.deltatime para manejar la hora

class Dispositivo(BaseModel):
    estado = TextField()
    fechaRegistro = DateTimeField()
    id= TextField()
    mac = TextField()
    nombre = TextField()
    propiedadComun = IntegerField()
    propiedadHorizontal = IntegerField()
    tipo = TextField()


class Persona(BaseModel):
    numeroIdentificacion = TextField()
    tipoIdentificacion = TextField()
    codigoSeguridad = TextField(null=True)
    huellaDigital = TextField(null=True)
    placasVehiculares = ListField(default=[])

    class Meta:
        primary_key = CompositeKey('numeroIdentificacion', 'tipoIdentificacion')


class Usuario(BaseModel):
    refresh = TextField()
    id = IntegerField(unique=True)
    password=TextField(null=True)
    email = TextField()
    token = TextField()
    roles = ListField()