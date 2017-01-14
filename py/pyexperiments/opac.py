import urllib
import urllib2

#uri='http://192.168.7.2/OPAC/memberstatus.aspx'

response = urllib.urlopen('http://python.org/')
html = response.read()
print html
