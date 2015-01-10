#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Importamos el servicio de usuarios para que la aplicacion se integre con las
#   cuentas de usuario de Google.
from google.appengine.api import users

# Importamos el marco de trabajo de aplicaciones web.
import webapp2


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
        self.response.write(casillaNombre('Nombre de prueba'))

                    

#==============================================================================
#==============================================================================
# # Métodos para dibujar una tabla.
#==============================================================================
#==============================================================================
def casillaNombre(texto, anchura="111.75"):
    """
    Este método se encarga de hacer una celda en HTML donde el texto tiene
    las siguientes propiedades:
        - Alineado a la izquierda.
        - Está en negrita.
        - Fondo azul.
        - Líneas superior e inferior.
    """
    # Comenzamos la creacion de la celda y le asignamos el ancho.
    celda = """<td width=149 valign=top style='width:""" + anchura 
    + """pt;border-top:solid windowtext 2.25pt;
          border-left:none;border-bottom:solid windowtext 2.25pt;border-right:none;
          background:#4BACC6;mso-background-themecolor:accent5;padding:0cm 5.4pt 0cm 5.4pt'>
					<p class=MsoNormal align=right
						style='margin-bottom:0cm;margin-bottom:.0001pt;
                          text-align:right;line-height:normal;mso-yfti-cnfc:517'>
						<b>
							<span style='color:white;mso-themecolor:background1'>
                                    """ + str(texto) + """<o:p></o:p>
							</span>
						</b>
					</p>
				</td>"""

    return celda

# WSGIApplication se encarga de instanciar las ruas de las solicitudes
#   entrantes a los manipuladores basados en la URL.
# La informacion acerca de la solicitud se puede obtener usando 'self.request'.
# debug=True sirve para imprimir la traza de la pila en la salida del 
#   navegador.
application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)