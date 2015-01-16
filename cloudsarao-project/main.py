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
import jinja2
import os
import logging # Para DEBUG

IMAGEN = '<img class="centrado" src="/img/header.jpg" alt="header">'
CSS = """<head><link rel="stylesheet" type="text/css" href="css/style.css">""" + IMAGEN + """</head>"""



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)



#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'MainPage'.
#==============================================================================
#==============================================================================
# RequestHandler se encarga de procesar las peticiones y contruir respuestas.
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>SARAOS AÑADIDOS</h1>')
        for i in Sarao.getSaraos():
            self.response.write("<p>Nombre: " + i.nombre + "</p>")
            self.response.write("<p>Max_asistentes: " + str(i.max_asistentes) + "</p>")
            self.response.write("<p>Fecha: " + str(i.fecha) + "</p>")
            self.response.write("<br>")

    def post(self):
        self.response.write('<html><body><h1>Petición POST</h1></body></html>')



#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'Saraos'.
#==============================================================================
#==============================================================================
class NuevoSarao(webapp2.RequestHandler):
    def post(self):
        # Obtenemos los parámetros enviados por POST
        Sarao(nombre = cgi.escape(self.request.get('nombre')),
              fecha = (datetime.datetime.strptime(cgi.escape(self.request.get('fecha')), '%m/%d/%Y')).date(), #Casting a datetime format
              #hora = cgi.escape(self.request.get('hora')),
              max_asistentes = int(cgi.escape(self.request.get('max_asistentes'))),
              url = cgi.escape(self.request.get('url')),
              nota = cgi.escape(self.request.get('nota')),
              descripcion = cgi.escape(self.request.get('descripcion'))
              #organizacion = cgi.escape(self.request.get('organizacion'))
              #lugar = cgi.escape(self.request.get('lugar'))
        ).put()
        self.response.write("Añadido sarao.")

    def get(self):
        self.render("insertar_sarao.html")

    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def realizaAlgunaOperacionGuay(self, numero):
        return numero*numero/2



class NuevoLugar(webapp2.RequestHandler):
    def post(self):
        Lugar(nombre = cgi.escape(self.request.get('nombre')),
              calle = cgi.escape(self.request.get('calle')),
              cp = cgi.escape(self.request.get('cod_postal'))).put()
        self.response.write("Añadido lugar.")

    def get(self):
        self.render("insertar_lugar.html")

    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))


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
