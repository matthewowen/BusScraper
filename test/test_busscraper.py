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

	def testGetStopsForPostcode(self):

		f = busscraper.postcode("ox41bz", "oxfordshire")

		self.assertTrue(type(f) is list)

		i = f[0]

		if i:
			self.assertTrue(type(i['stop_name']) is unicode)
			self.assertTrue(type(i['stop_id']) is unicode)
			self.assertTrue(type(i['distance']) is int)
		else:
			pass

	def testGetStopsOnService(self):

		f = busscraper.service("2", "5", "Blackbird+Leys", "oxfordshire", "35")

		self.assertTrue(type(f) is list)

		i = f[0]

		if i:
			self.assertTrue(type(i['stop_name']) is unicode)
			self.assertTrue(type(i['stop_id']) is unicode)

if __name__ == '__main__':
    unittest.main()