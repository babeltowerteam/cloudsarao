from google.appengine.api import users

# Importamos el marco de trabajo de aplicaciones web.
import webapp2

#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'MainPage'.
#==============================================================================
#==============================================================================
# RequestHandler se encarga de procesar las peticiones y contruir respuestas.
class MainPage(webapp2.RequestHandler):

    def get(self):
        # [START get_current_user]
        # Checks for active Google account session
        user = users.get_current_user()
        # [END get_current_user]

        # [START if_user]
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        # [END if_user]
        # [START if_not_user]
        else:
            self.redirect(users.create_login_url(self.request.uri))
        # [END if_not_user]

#==============================================================================
#==============================================================================
# # Controlador de solicitudes 'Saraos'.
#==============================================================================
#==============================================================================
class Saraos(webapp2.RequestHandler):
    def get(self):
        self.response.write('Web Sarao')


#==============================================================================
#==============================================================================
# # Programa principal.
#==============================================================================
#==============================================================================
# WSGIApplication se encarga de instanciar las ruas de las solicitudes
#   entrantes a los manipuladores basados en la URL.
# Asignamos el controlador de solicitudes (MainPage) a la URL raiz (/), de modo
#   que cuando 'webapp2' recibe una solicitud 'GET HTTP' a la URL '/' se crea
#   una instancia de la clase 'MainPage' y llama a al método 'get'.
# La informacion acerca de la solicitud se puede obtener usando 'self.request'.
# Asignamos el controlador de solicitudes (Saraos) a la URL '/saraos'.
# debug=True sirve para imprimir la traza de la pila en la salida del 
#   navegador.
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/saraos', Saraos),
], debug=True)
