import unittest
from google.appengine.api import users
from main import Sarao

class SaraoTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test(self):
		sarao = Sarao()
		res = sarao.realizaAlgunaOperacionGuay(4)
		self.assertEqual(res,8)


if __name__ == "__main__":
	unittest.main()
