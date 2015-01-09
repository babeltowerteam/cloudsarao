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
    def dibujarTabla(self):
        self.response.write("""<body lang=ES style='tab-interval:35.4pt'>

    <div class=WordSection1>

        <table class=MsoTableMediumShading2Accent5 border=1 cellspacing=0
            cellpadding=0
            style='border-collapse:collapse;border:none;mso-border-top-alt:
 solid windowtext 2.25pt;mso-border-bottom-alt:solid windowtext 2.25pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
            <tr style='mso-yfti-irow:-1;mso-yfti-firstrow:yes'>
                <td width=149 valign=top
                    style='width:111.75pt;border-top:solid windowtext 2.25pt;
  border-left:none;border-bottom:solid windowtext 2.25pt;border-right:none;
  background:#4BACC6;mso-background-themecolor:accent5;padding:0cm 5.4pt 0cm 5.4pt'>
                    <p class=MsoNormal align=right
                        style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal;mso-yfti-cnfc:517'>
                        <b>
                            <span style='color:white;mso-themecolor:background1'>
                                Nombre
                                <o:p></o:p>
                            </span>
                        </b>
                    </p>
                </td>
                <td width=113 valign=top
                    style='width:3.0cm;border-top:solid windowtext 2.25pt;
  border-left:none;border-bottom:solid windowtext 2.25pt;border-right:none;
  background:#4BACC6;mso-background-themecolor:accent5;padding:0cm 5.4pt 0cm 5.4pt'>
                    <p class=MsoNormal
                        style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal;mso-yfti-cnfc:1'>
                        <b>
                            <span style='color:white;mso-themecolor:background1'>
                                Fecha
                                <o:p></o:p>
                            </span>
                        </b>
                    </p>
                </td>
            </tr>
            <tr style='mso-yfti-irow:0'>
                <td width=149 valign=top
                    style='width:111.75pt;border:none;background:#4BACC6;
  mso-background-themecolor:accent5;padding:0cm 5.4pt 0cm 5.4pt'>
                    <p class=MsoNormal align=right
                        style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal;mso-yfti-cnfc:68'>
                        <b>
                            <span style='color:white;mso-themecolor:background1'>
                                <o:p>&nbsp;
                                </o:p>
                            </span>
                        </b>
                    </p>
                </td>
                <td width=113 valign=top
                    style='width:3.0cm;border:none;background:#D8D8D8;
  mso-background-themecolor:background1;mso-background-themeshade:216;
  padding:0cm 5.4pt 0cm 5.4pt'>
                    <p class=MsoNormal
                        style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal;mso-yfti-cnfc:64'>
                        <o:p>&nbsp;
                        </o:p>
                    </p>
                </td>
            </tr>
            <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes'>
                <td width=149 valign=top
                    style='width:111.75pt;border:none;border-bottom:
  solid windowtext 2.25pt;background:#4BACC6;mso-background-themecolor:accent5;
  padding:0cm 5.4pt 0cm 5.4pt'>
                    <p class=MsoNormal align=right
                        style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal;mso-yfti-cnfc:4'>
                        <b>
                            <span style='color:white;mso-themecolor:background1'>
                                <o:p>&nbsp;
                                </o:p>
                            </span>
                        </b>
                    </p>
                </td>
                <td width=113 valign=top
                    style='width:3.0cm;border:none;border-bottom:solid windowtext 2.25pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
                    <p class=MsoNormal
                        style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>
                        <o:p>&nbsp;
                        </o:p>
                    </p>
                </td>
            </tr>
        </table>

        <p class=MsoNormal>
            <o:p>&nbsp;
            </o:p>
        </p>

    </div>

</body>""")

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

            sarao = tablaSarao(nombre=str(user), fecha=datetime.datetime.now().date(), max_asistentes=10, num_asistentes=10, url='http://www.google.es', nota='sarao_prueba')
            sarao.put()
            saraos = db.GqlQuery("SELECT * FROM tablaSarao")
            self.response.write("<h1>ULTIMOS VISITANTES</h1>")
            for i in saraos:
                self.response.write("<p>" + i.nombre + " a las " + str(i.fecha) + "</p>")

            self.response.write('</div></body></html>')

            # Dibujamos una tabla.
            self.dibujarTabla()

        # Si no hay una cuenta activa.
        else:
            # Le mandamos a la pagina de login.
            self.redirect(users.create_login_url(self.request.uri))

#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'Saraos'.
#==============================================================================
#==============================================================================
class Sarao(webapp2.RequestHandler):
    def get(self):
        self.response.write('Web Sarao')

    def realizaAlgunaOperacionGuay(self, numero):
        return numero*numero/2

#==============================================================================
#==============================================================================
# # Clase tablaSarao
#==============================================================================
#==============================================================================

class tablaSarao(db.Model):
    # Esta clase tiene los siguientes atributos:
    # - nombre : Nombre del Sarao.
    # - fecha : Fecha de realizacion del Sarao.
    # - max_asistentes : El numero máximo de asistentes que puede asistir al
    #                   Sarao.
    # - num_asistentes : Número de asistentes que están apuntados al Sarao.
    # - url : Dirección web del Sarao.
    # - nota : Todo tipo de notas explicativas asociadas al Sarao. 
    nombre          = db.StringProperty()
    fecha           = db.DateProperty()
    max_asistentes  = int()
    num_asistentes  = int()
    url             = db.StringProperty()
    nota            = db.StringProperty()


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
    ('/saraos', Sarao),
], debug=True)
