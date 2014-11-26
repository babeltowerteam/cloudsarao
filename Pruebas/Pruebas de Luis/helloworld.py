# Importamos el marco de trabajo de aplicaciones web.
import webapp2

# Definimos un controlador de solicitudes (MainPage).
#   RequestHandler se encarga de procesar las peticiones y contruir respuestas.
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

# WSGIApplication se encarga de instanciar las ruas de las solicitudes
#   entrantes a los manipuladores basados en la URL.
# Asignamos el controlador de solicitudes (MainPage) a la URL raiz (/), de modo
#   que cuando 'webapp2' recibe una solicitud 'GET HTTP' a la URL '/' se crea
#   una instancia de la clase 'MainPage' y llama a al método 'get'.
# La informacion acerca de la solicitud se puede obtener usando 'self.request'.
# debug=True sirve para imprimir la traza de la pila en la salida del 
#   navegador.
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)