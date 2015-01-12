#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db

#==============================================================================
#==============================================================================
# # Clase Lugar
#==============================================================================
#==============================================================================
class Lugar(db.Model):
    nombre = db.StringProperty(required=True)
    calle = db.IntegerProperty(required=True)
    cod_postal = db.IntegerProperty()


#==============================================================================
#==============================================================================
# # Clase Sarao
#==============================================================================
#==============================================================================
# Esta clase tiene los siguientes atributos:
# - nombre : Nombre del Sarao.
# - fecha : Fecha de realizacion del Sarao.
# - max_asistentes : El numero máximo de asistentes que puede asistir al
#                   Sarao.
# - num_asistentes : Número de asistentes que están apuntados al Sarao.
# - url : Dirección web del Sarao.
# - nota : Todo tipo de notas aclaratorias asociadas al Sarao.
# - descripcion : Descripción del evento.
class Sarao(db.Model):
  # Atributos del sarao.
    nombre         = db.StringProperty(required=True)
    fecha          = db.DateProperty(required=True)
    hora           = db.DateProperty()
    max_asistentes = db.IntegerProperty(required=True)
    num_asistentes = db.IntegerProperty()
    url            = db.StringProperty(required=True)
    nota           = db.StringProperty()
    descripcion    = db.TextProperty()
    organizacion   = db.StringProperty()
    limite_inscripcion = db.DateProperty()
    # Relación uno-a-muchos
    #lugar          = db.ReferenceProperty(Lugar, collection_name='lugares')

    @property
    def asistentes(self):
        return Asistente.gql("WHERE asistencia_saraos = :1", self.key())

    @classmethod
    def getSaraos(self):
        return self.all()



#==============================================================================
#==============================================================================
# # Clase Asistente
#==============================================================================
#==============================================================================
class Asistente(db.Model):
    correo = db.EmailProperty(required=True)
    nombre = db.StringProperty(required=True)
    nick_twitter = db.StringProperty()
    colectivo = db.StringProperty(required=True, choices=('alumno', 'PDI', 'PAS', 'otro'))
    procedencia = db.StringProperty()
    #Relacion muchos-muchos de saraos y asistentes
    asistencia_saraos = db.ListProperty(db.Key)
