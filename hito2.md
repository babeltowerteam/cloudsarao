## Hito 2

El primer paso ha sido crear el proyecto de la Google App Engine **cloudsarao**. Por el momento es un proyecto simple, estilo *hola mundo* cuya única funcionalidad consiste en obtener la cuenta de correo de aquel que quiere acceder y tomarla como nombre del usuario para saludarle.

El proyecto en GAE contiene una clase principal **MainPage** dentro del fichero principal y un fichero de configuración **app.yaml**. Éste fichero de configuración contiene los siguientes datos:

* Identificador de la aplicación
* Versión de la aplicación
* Versión de la api
* Manejadores de urls, usuarios, etc
* Librerías que utiliza el proyecto


El segundo paso ha sido desplegar el proyecto en los servidores de Google y comprobar que funciona. Para acceder a la aplicación desplegada pinchar [aquí](http://cloudsarao.appspot.com/)


El último paso ha sido introducir la **Integración contínua**. Para este fin hemos utilizado la plataforma [Shippable](https://www.shippable.com/). Esta plataforma nos permite, al ejecutar un comando *push* en nuestro repositorio del proyecto, realizar los tests necesarios y el despliegue de la aplicación en caso de pasar las pruebas.
Para que esto funcione, es necesario tener un fichero de configuración **shippable.yml** dentro de la raíz del repositorio.

[Ejemplo de integración contínua CON **Shippable** y Google App Engine (Python)](https://github.com/shippableSamples/sample-python-datastore-appengine/blob/master/shippable.yml)