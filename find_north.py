
from xml.etree.ElementTree import parse

office_lat = 41.900262
doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat >= office_lat:
        busid = bus.findtext('id')
        direction = bus.findtext('d')
        if direction.startswith('North'):
            print(busid, direction, lat)







