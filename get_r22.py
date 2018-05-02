import urllib
import webbrowser
from xml.etree.ElementTree import parse

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write (data)
f.close()


