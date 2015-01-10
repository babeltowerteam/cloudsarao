#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Importamos el servicio de usuarios para que la aplicacion se integre con las
#   cuentas de usuario de Google.
from google.appengine.api import users

# Importamos el marco de trabajo de aplicaciones web.
import webapp2
from maquetacionTabla import *


MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""

# Definimos un controlador de solicitudes (MainPage).
#   RequestHandler se encarga de procesar las peticiones y contruir respuestas.
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.write(casillaNombre('Nombre de prueba'))
        self.response.write(MAIN_PAGE_HTML)
        self.response.write(casillaNombre('Nombre!'))
                    

# WSGIApplication se encarga de instanciar las ruas de las solicitudes
#   entrantes a los manipuladores basados en la URL.
# La informacion acerca de la solicitud se puede obtener usando 'self.request'.
# debug=True sirve para imprimir la traza de la pila en la salida del 
#   navegador.
application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)