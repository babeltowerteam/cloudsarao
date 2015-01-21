#!/usr/bin/env python
# -*- coding: utf-8 -*-

CABECERA = """<html><head></head><body>"""
FIN_CABECERA = """</body></html>"""

class FormularioNuevoSarao():
  def parseFormulario(self):
    return CABECERA + """
        <form action="" method="post">
            Ingrese su nombre:
            <input type="text" name="nombre"><br>
            <input type="submit" value="Enviar"><br>
        </form>
        """ + FIN_CABECERA


class FormularioNuevoAsistente():
    def parseFormulario(self):
        return ""
