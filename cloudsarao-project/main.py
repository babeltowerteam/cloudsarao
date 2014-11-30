# Importamos el servicio de usuarios para que la aplicacion se integre con las
#   cuentas de usuario de Google.
from google.appengine.api import users

# Importamos el marco de trabajo de aplicaciones web.
import webapp2

IMAGEN = '<img src="/img/img.jpg" alt="header" width="100" height="100">'

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
            self.response.write("<html><body>")
            self.response.write(IMAGEN)
            self.response.write('<br></br>')
            self.response.write('Hello, ' + user.nickname())
            self.response.write('</body></html>')

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
