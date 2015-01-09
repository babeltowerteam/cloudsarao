#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos el servicio de usuarios para que la aplicacion se integre con las
#   cuentas de usuario de Google.
from google.appengine.api import users
import datetime
from google.appengine.ext import db

# Importamos el marco de trabajo de aplicaciones web.
import webapp2

IMAGEN = '<img class="centrado" src="/img/header.jpg" alt="header">'
CSS = """<head><link rel="stylesheet" type="text/css" href="css/style.css">""" + IMAGEN + """</head>"""

#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'MainPage'.
#==============================================================================
#==============================================================================
# RequestHandler se encarga de procesar las peticiones y contruir respuestas.
class MainPage(webapp2.RequestHandler):
    def get(self):
        # Comprobamos que hay una cuenta de Google activa.
        user = users.get_current_user()


        # Si esta activo el usuario.
        if user:
            #self.response.headers['Content-Type'] = 'text/plain'
            # Le saludamos con su nombre.
            self.response.write('<html>'+CSS+'<div id="contenido"><body>')
            self.response.write('<br></br>')
            self.response.write('Hello, ' + user.nickname())

            sarao = Sarao(nombre=str(user), fecha=datetime.datetime.now().date(), max_asistentes=10, num_asistentes=10, url='http://www.google.es', nota='sarao_prueba')
            sarao.put()
            saraos = db.GqlQuery("SELECT * FROM Sarao")
            self.response.write("<h1>ULTIMOS VISITANTES</h1>")
            for i in saraos:
                self.response.write("<p>" + i.nombre + " a las " + str(i.fecha) + "</p>")

            self.response.write('</div></body></html>')

        # Si no hay una cuenta activa.
        else:
            # Le mandamos a la pagina de login.
            self.redirect(users.create_login_url(self.request.uri))

#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'Saraos'.
#==============================================================================
#==============================================================================
class WebSarao(webapp2.RequestHandler):
    def get(self):
        self.response.write('Web Sarao')

    def realizaAlgunaOperacionGuay(self, numero):
        return numero*numero/2

#==============================================================================
#==============================================================================
# # Clase tablaSarao
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
    max_asistentes = db.IntegerProperty(required=True)
    num_asistentes = db.IntegerProperty()
    url            = db.StringProperty(required=True)
    nota           = db.StringProperty()
    descripcion    = db.TextProperty()

    lugar = db.ReferenceProperty(db.Key, collection_name='lugares')
    


#==============================================================================
#==============================================================================
# # Clase tablaLugares
#==============================================================================
#==============================================================================

class Lugar(db.Model):

    calle = db.StringProperty(required=True)
    numero = db.IntegerProperty(required=True)
    cod_postal = db.IntegerProperty()

#==============================================================================
#==============================================================================
# # Clase tablaAsistente
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

#==============================================================================
#==============================================================================
# # Programa principal.
#==============================================================================
#==============================================================================
# WSGIApplication se encarga de instanciar las ruas de las solicitudes
#   entrantes a los manipuladores basados en la URL.
# Asignamos el controlador de solicitudes (MainPage) a la URL raiz (/), de modo
#   que cuando 'webapp2' recibe una solicitud 'GET HTTP' a la URL '/' se crea
# La informacion acerca de la solicitud se puede obtener usando 'self.request'.
# Asignamos el controlador de solicitudes (Saraos) a la URL '/saraos'.
# debug=True sirve para imprimir la traza de la pila en la salida del
#   navegador.
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/saraos', WebSarao),
], debug=True)
