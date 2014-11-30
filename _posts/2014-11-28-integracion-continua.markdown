---
layout: post
title:  "Misión Integración Continua: completada!!!"
date:   2014-11-28
author: <a href="https://github.com/sergiogvz">sergiogvz</a>
categories: Desarrollo
---

Ya ha costado, pero por fin, se ha conseguido. Se ha montado una plataforma de integración continua para el proyecto CloudSarao.
Con ayuda de la plataforma (Shippable)[http://www.shippable.com], para los amigos shiPablo, hemos conseguido enlazar los push de nuestro repositorio master, para que, automáticamente, se realicen una serie de test sobre la aplicación y, en el caso de pasarlos, se despliegue con GAE.

Si quieres ver como se ha configurado, te aconsejamos mirar con detenimiento los archivos [requirements.txt](https://github.com/babeltowerteam/cloudsarao/blob/master/requirements.txt), [shippable.yml](https://github.com/babeltowerteam/cloudsarao/blob/master/shippable.yml) y [test.py](https://github.com/babeltowerteam/cloudsarao/blob/master/cloudsarao-project/test.py) que se encuentran en nuestro [repo](https://github.com/babeltowerteam/cloudsarao).

Con esto, concluimos el [hito 2](https://github.com/babeltowerteam/cloudsarao/blob/master/hito2.md) de nuestro proyecto. yay!! :D

Manteneros atentos al progreso de CloudSarao!!!;)
