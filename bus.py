import urllib
import webbrowser
from xml.etree.ElementTree import parse

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write (data)
f.close()

office_lat = 41.980262
longitude = -87.668452


close_distance =100

doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat >= office_lat:
        busid = bus.findtext('id')
        direction = bus.findtext('d')
        if direction.startswith('North'):
            print(busid, direction, lat)





