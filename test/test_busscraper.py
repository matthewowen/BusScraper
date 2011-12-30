import unittest

import busscraper

class testScraper(unittest.TestCase):
	"""
	Test class for the BusScraper module
	"""

	def testGetBusesForStop(self):

		f = busscraper.stop("69323635", "oxfordshire")
			
		self.assertTrue(type(f) is list)

		i = f[0]

		if i:
			self.assertTrue(type(i['minutes_to_departure']) is int)
			self.assertTrue(type(i['destination']) is unicode)
			self.assertTrue(type(i['service']) is unicode)
		else:
			pass

if __name__ == '__main__':
    unittest.main()