#Especificación de la base de datos


- Sarao
    + nombre *
    + fecha *
    + hora
    + max_asistentes *
    + num_asistentes
    + url *
    + nota
    + descripcion
    + organizacion
    + limite_inscripcion *
    + lugar (atributo relación con la tabla Lugar) *

- Lugar
    + nombre *
    + calle *
    + cod_postal


- Asistente
    + correo *
    + nombre *
    + nick_twitter
    + colectivo *
    + procedencia
    + asistencia_saraos (atributo relación con saraos)