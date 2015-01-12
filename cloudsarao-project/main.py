#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos el servicio de usuarios para que la aplicacion se integre con las
#   cuentas de usuario de Google.
from google.appengine.api import users
import datetime
# Importamos el archivo persistence.py, que contiene las clases para la persistencia
from persistence import *
from formulario import *

# Importamos el marco de trabajo de aplicaciones web.
import webapp2
import cgi

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

        # Crea un formulario y lo muestra
        #self.response.write(FormularioNuevoSarao().parseFormulario())


        # Si esta activo el usuario.
        if user:
            #self.response.headers['Content-Type'] = 'text/plain'
            # Le saludamos con su nombre.
            self.response.write('<html>'+CSS+'<div id="contenido"><body>')
            self.response.write('<br></br>')
            self.response.write('Hello, ' + user.nickname())

            sarao = Sarao(nombre=str(user),
                          fecha=datetime.datetime.now().date(),
                          max_asistentes=10,
                          num_asistentes=10,
                          url='http://www.google.es',
                          nota='sarao_prueba')
            sarao.put()
            """
            saraos = db.GqlQuery("SELECT * FROM Sarao")
            self.response.write("<h1>SARAOS</h1>")
            """
            for i in Sarao.getSaraos():
                self.response.write("<p>" + i.nombre + " a las " + str(i.fecha) + "</p>")

            self.response.write('</div></body></html>')

        # Si no hay una cuenta activa.
        else:
            # Le mandamos a la pagina de login.
            self.redirect(users.create_login_url(self.request.uri))


    def post(self):
        self.response.write('<html><body><h1>Petición POST</h1></body></html>')
        # Obtenemos los parámetros enviados por POST
        nom = cgi.escape(self.request.get('nombre'))
        self.response.out.write("Nombre: "+ nom + "<br>")


#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'Saraos'.
#==============================================================================
#==============================================================================
class NuevoSarao(webapp2.RequestHandler):
    def post(self):
        # Obtenemos los parámetros enviados por POST
        Sarao(nombre = cgi.escape(self.request.get('nombre')),
              fecha = cgi.escape(self.request.get('fecha')),
              hora = cgi.escape(self.request.get('hora')),
              max_asistentes = cgi.escape(self.request.get('max_asistentes')),
              url = cgi.escape(self.request.get('url')),
              nota = cgi.escape(self.request.get('nota')),
              descripcion = cgi.escape(self.request.get('descripcion')),
              organizacion = cgi.escape(self.request.get('organizacion'))
              #lugar = cgi.escape(self.request.get('lugar'))
        ).put()
        self.response.write("Añadido sarao.")

    def get(self):
        self.response.write('Web Sarao')

    def realizaAlgunaOperacionGuay(self, numero):
        return numero*numero/2


class NuevoLugar(webapp2.RequestHandler):
    def post(self):
        Lugar(nombre = cgi.escape(self.request.get('nombre')),
              calle = cgi.escape(self.request.get('calle')),
              cp = cgi.escape(self.request.get('cod_postal'))
        ).put()
        self.response.write("Añadido lugar.")

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
    ('/nuevosarao', NuevoSarao),
    ('/nuevolugar', NuevoLugar),
], debug=True)
