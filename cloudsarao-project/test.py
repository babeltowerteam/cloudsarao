
#import sys
#sys.path.append('/tmp/gae/google_appengine/google/appengine')

#from api import *
#from ext import *
#from ext import db
#from runtime import *
import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from persistence_tests import *


class SaraoTestCase(unittest.TestCase):
	def setUp(self):
		self.testbed = testbed.Testbed()
		self.testbed.activate()
		self.testbed.init_datastore_v3_stub()

		lugar = Lugar(nombre="Lugar de prueba", calle="Calle de prueba", cod_postal=6666)
		lugar.put()



	def tearDown(self):
		self.testbed.desactivate()


	def testInsertarSarao(self):
		sarao = Sarao(nombre="Sarao de prueba", fecha="11\11\2009", max_asistentes=11, lugar = lugar)
		sarao.put()
		sarao = Sarao.gql("WHERE nombre = :n", n=sarao.nombre)
		sarao.delete()

	def testInsertarLugar(self):
		lugar = Lugar(nombre="testLugar", calle="testCalle", cod_postal=1111)
		lugar.put()
		lugar = Lugar.gql("WHERE nombre = :n", n=lugar.nombre)
		lugar.delete()

if __name__ == "__main__":
	unittest.main()
