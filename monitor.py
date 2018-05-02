import urllib
from xml.etree.ElementTree import parse
candidates = ['4133','4165','1877']
office_lat = 41.900262

def distance(lat1, lat2):
    #return distance in mile sbetween two lats
    return 69*abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, office_lat)
            print busid, dis, 'miles'
    print '-'*10

import time
while True:
    monitor()
    time.sleep(60)
