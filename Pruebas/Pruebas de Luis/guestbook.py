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
        self.response.write(MAIN_PAGE_HTML)

            
class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')            

# WSGIApplication se encarga de instanciar las ruas de las solicitudes
#   entrantes a los manipuladores basados en la URL.
# Asignamos el controlador de solicitudes (MainPage) a la URL raiz (/), de modo
#   que cuando 'webapp2' recibe una solicitud 'GET HTTP' a la URL '/' se crea
#   una instancia de la clase 'MainPage' y llama a al metodo 'get'.
# La informacion acerca de la solicitud se puede obtener usando 'self.request'.
# debug=True sirve para imprimir la traza de la pila en la salida del 
#   navegador.
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)