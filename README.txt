===========
Bus Scraper
===========

Bus Scraper allows you to scrape bus times and information from ACIS powered bus time sites (like the Oxfordshire, South Yorkshire, Bristol, and Kent ones). If they change the markup of their pages, it might break.

    #!/usr/bin/env python

    import busscraper

    busscraper.stop("37035419", "tsy")
        [{'minutes_to_departure': 0, 'destination': u'Rotherham&nbsp;', 'service': u'220&nbsp;'}, {'minutes_to_departure': 30, 'destination': u'Doncaster&nbsp;', 'service': u'222&nbsp;'}, {'minutes_to_departure': 30, 'destination': u'Rotherham&nbsp;', 'service': u'220&nbsp;'}, {'minutes_to_departure': 0, 'destination': u'Rotherham&nbsp;', 'service': u'229&nbsp;'}]
    
    busscraper.postcode("s637tg", "tsy")
		[{'distance': 107, 'stop_name': u'Pope Pius School', 'stop_id': u'37035419'}, {'distance': 168, 'stop_name': u'Pope Pius School', 'stop_id': u'37035385'}]

	busscraper.service("2", "5", "Blackbird+Leys", "oxfordshire", "35")
		[{'stop_name': u'Oxford Rail Stn R2', 'stop_id': u'69326565&pscode=5&dest=&textonly=1'}, {'stop_name': u'Frideswide Sq R7', 'stop_id': u'340002070R7&pscode=5&dest=&textonly=1'}, {'stop_name': u'New Road D1', 'stop_id': u'340000868D1&pscode=5&dest=&textonly=1'}, {'stop_name': u'Castle Street M1', 'stop_id': u'340000007M1&pscode=5&dest=&textonly=1'}, {'stop_name': u'Speedwell St S2', 'stop_id': u'340001989S2&pscode=5&dest=&textonly=1'}, {'stop_name': u"St Aldate's G4", 'stop_id': u'69326475&pscode=5&dest=&textonly=1'}, {'stop_name': u"Queen's Lane K1", 'stop_id': u'340001992K1&pscode=5&dest=&textonly=1'}, {'stop_name': u'The Plain', 'stop_id': u'340001126TYN&pscode=5&dest=&textonly=1'}, {'stop_name': u'James Street', 'stop_id': u'340001199PEM&pscode=5&dest=&textonly=1'}, {'stop_name': u'Manzil Way', 'stop_id': u'340001198OUT&pscode=5&dest=&textonly=1'}, {'stop_name': u'Magdalen Road', 'stop_id': u'340001195OPP&pscode=5&dest=&textonly=1'}, {'stop_name': u'Howard Street', 'stop_id': u'340001197CNR&pscode=5&dest=&textonly=1'}, {'stop_name': u'Shelley Road', 'stop_id': u'69323639&pscode=5&dest=&textonly=1'}, {'stop_name': u'Marsh Road', 'stop_id': u'340001200OPH&pscode=5&dest=&textonly=1'}, {'stop_name': u'Clive Road', 'stop_id': u'340001201OPP&pscode=5&dest=&textonly=1'}, {'stop_name': u'Original Swan PH', 'stop_id': u'340001257BTW&pscode=5&dest=&textonly=1'}, {'stop_name': u'Templars Square', 'stop_id': u'69324978&pscode=5&dest=&textonly=1'}, {'stop_name': u'Barns Road', 'stop_id': u'340001251OPB&pscode=5&dest=&textonly=1'}, {'stop_name': u'Kersington Crescent', 'stop_id': u'340001225CNR&pscode=5&dest=&textonly=1'}, {'stop_name': u'Sandy Lane West', 'stop_id': u'340001230ERB&pscode=5&dest=&textonly=1'}, {'stop_name': u'Sandy Lane', 'stop_id': u'69325292&pscode=5&dest=&textonly=1'}, {'stop_name': u'Wingate Close', 'stop_id': u'340001234CNR&pscode=5&dest=&textonly=1'}, {'stop_name': u'Longlands Road', 'stop_id': u'340001229CNR&pscode=5&dest=&textonly=1'}, {'stop_name': u'Pegasus Court', 'stop_id': u'69325284&pscode=5&dest=&textonly=1'}]