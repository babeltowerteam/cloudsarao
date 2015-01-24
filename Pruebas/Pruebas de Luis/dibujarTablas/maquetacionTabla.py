#!/usr/bin/env python
# -*- coding: utf-8 -*-

#==============================================================================
#==============================================================================
# # Métodos para dibujar una tabla.
#==============================================================================
#==============================================================================

def inicioTabla():
    """
    Esta funcion devuelve la definicion de una tabla el inicio del texto en 
    HTML, indicando las etiquetas <body>, <div> y <table> que al final deverán
    cerrase.
    """
    texto = """
        <body lang=ES style='tab-interval:35.4pt'>
        	<div class=WordSection1>
    		<table class=MsoTableMediumShading2Accent5 border=1 cellspacing=0
    			cellpadding=0
    			style='border-collapse:collapse;border:none;mso-border-top-alt:
                   solid windowtext 2.25pt;mso-border-bottom-alt:solid windowtext 2.25pt;
                   mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
     """
    return texto
    
def finalTabla():
    """ 
    Esta funcion se encarga de devolver el final de la definicion de la
    tabla cerrando las primeras etiquetas.
    """
    texto = """</table> </div> </body> """
    return texto

def casillaNombre(texto, anchura="111.75"):
    """
    Este método se encarga de hacer una celda en HTML donde el texto tiene
    las siguientes propiedades:
        - Alineado a la izquierda.
        - Está en negrita.
        - Fondo azul.
        - Líneas superior e inferior.
    """
    # Comenzamos la creacion de la celda y le asignamos el ancho.
    celda = """<td width=149 valign=top style='width:""" + anchura +  """pt;border-top:solid windowtext 2.25pt;
          border-left:none;border-bottom:solid windowtext 2.25pt;border-right:none;
          background:#4BACC6;mso-background-themecolor:accent5;padding:0cm 5.4pt 0cm 5.4pt'>
					<p class=MsoNormal align=right
						style='margin-bottom:0cm;margin-bottom:.0001pt;
                          text-align:right;line-height:normal;mso-yfti-cnfc:517'>
						<b>
							<span style='color:white;mso-themecolor:background1'>
                                    """ + str(texto) + """<o:p></o:p>
							</span>
						</b>
					</p>
				</td>"""

    return celda

#==============================================================================
#==============================================================================
# # Código de pruebas.
#==============================================================================
#==============================================================================
if __name__== "__main__": 
    print(inicioTabla())