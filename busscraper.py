import httplib2
from BeautifulSoup import BeautifulSoup

def get_content(URL):
	"""
	gets content from URL and makes the markup valid
	"""

	http = httplib2.Http()
	resp, content = http.request(URL, "GET")
	soup = BeautifulSoup(content)

	return soup

def stop(stop_id, subdomain):

	"""
	returns all the buses for a given stop as a list of dictionaries
	"""

	URL = "http://%s.acislive.com/pip/stop.asp?naptan=%s&textonly=1" % (subdomain, stop_id)
	soup = get_content(URL)

	# find all the buses, distinguished by destination
	buses = soup.findAll('td', {'class': 'destination'})

	# establish list of buses and create dictionary of info for each bus
	bus_list = []

	for bus in buses:
		info = {}
		# make the destination a string
		destination = bus.string
		destination = destination.replace('&nbsp;', '')
		destination = unicode(destination)
		info['destination'] = destination
		# find the service name/number for each bus
		service = bus.findPreviousSibling()
		service = service.string
		service = service.replace('&nbsp;', '')
		service = unicode(service)
		info['service'] = service
		# find how many minutes until it departs
		m = bus.findNextSibling('td')
		m = m.string
		# convert minutes into integer, with a value of 0 for due
		m = m.replace(' mins', '')
		m = m.replace('&nbsp;', '')
		try:
			m = int(m)
		except ValueError:
			m = 0
		info['minutes_to_departure'] = m
		# add dictionary to list
		bus_list.append(info)

	return bus_list

def postcode(postcode, subdomain):

	"""
	returns all the stops near a given postcode as a list of dictionaries
	"""

	URL = "http://%s.acislive.com/web/postcode.asp?postcode=%s&textonly=1" % (subdomain, postcode)
	soup = get_content(URL)
	# identify individual stops by finding <a> in <td>
	# remove pagination
	pager = soup.find('td', {'colspan': '6', 'align': 'center'})
	pager.extract()

	table = soup.find('table', {'id': 'Table3'})
	stops = table.findAll('a', )

	# establish list of stops and create dictionary of info for each stop
	stop_list = []
	for stop in stops:
		info = {}
		# make the stop a string
		stop_name = stop.string
		stop_name = unicode(stop_name)
		info['stop_name'] = stop_name
		# provide the stop id
		s = stop['href']
		s = s.replace('/pip/stop.asp?naptan=', '')
		s = s.replace('&textonly=1', '')
		s = unicode(s)
		info['stop_id'] = s
		# provide the distance as number
		d = stop.findParent()
		d = d.findPreviousSibling()
		d = d.findPreviousSibling()
		d = d.string
		d = d.replace(' metres', '')
		d = int(d)
		info['distance'] = d
		# add dictionary to list
		stop_list.append(info)
	
	return stop_list

def service(operator, service, destination, subdomain, systemid):
	"""
	returns all the stops on a particular service as a list of dictionaries
	"""

	URL = "http://%s.acislive.com/web/public_service_stops.asp?service=%s&operatorid=%s&systemid=%s&goingto=%s&showall=1&textonly=1" % (subdomain, service, operator, systemid, destination)
	soup = get_content(URL)

	# remove collapsers and isolate the relevant table
	collapsers = soup.findAll('a', {'class': 'noline'})
	[collapser.extract() for collapser in collapsers]
	table = soup.find('table')

	# find the stops,  create the list of dictionaries
	stops = table.findAll('a', )
	
	stop_list = []

	for stop in stops:
		info = {}
		stop_name = stop.string
		stop_name = unicode(stop_name)
		info['stop_name'] = stop_name
		# find the stop number from the href, some stops don't have numbers
		try:
			s = stop['href']
			s = s.replace('/pip/stop.asp?naptan=', '')
			s = s.replace('&pscode=1&dest=&textonly=1', '')
			s = s.partition('&')[0]
			s = unicode(s)
		except KeyError:
			s = ''
		info['stop_id'] = s
		# add dictionary to list
		stop_list.append(info)

	return stop_list