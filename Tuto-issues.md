#¿Cómo trabajar correctamente con los issues y relacionarlos a las tareas del proyecto?

Básicamente la idea es que cada tarea que suponga añadir y modificar ficheros debe de estar representado en un issue. Por tanto, cada vez que se haga un commit para completar parte de la tarea, se ha de hacer referencia a dicho Issue. Cuando la tarea se ha terminado, el issue correspondiente se ha de cerrar con un commit, que si puede reflejar lo último modificado, mejor que mejor. Todo esto, desde lineas de comandos. Esto me lo explico JJ y un buen ejemplo de ello es el siguiente:
- Él creo un issue para indicar la tarea de aprender a utilizar issues.
- Después en el fichero TODO.md, indicó una linea, para mostrar teníamos esa tarea que hacer y dicho commit lo refirió al issue de la siguiente manera: 
```
  git commit -am "Probando issues desde cli REFERENCES #9".
```
La # nos permite linkar el mensaje al issue apareciendo en él. El REFERENCES lo puedes obviar, eso es simplemente para indicar que existe una referencia.
- Tras esto, modificó en el TODO.md poniéndole el TICK y cerrando el issue con un commit:
```
  git commit -am "Aprendido closes #9"
```
La palabra closes, close, fix,... permiten cerrar el issue #N desde el propio mensaje del commit.

Espero que me haya explicado bien :)