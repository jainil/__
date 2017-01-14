import urllib
import json

def ex_region(dct):
    for result in dct:
        if "administrative_area_level_2" in result('types'):
            return result("long name")

def wget(url):
    try:
        ufile = urllib.urlopen(url)
	#print ufile.info().gettype()
        if ufile.info().gettype() == 'application/json':
            file_json = json.loads(ufile.read(), object_hook=ex_region)
            #values = json.dumps(file_json, sort_keys=True, indent=4)
            #print values
            print file_json
    except IOError:
        print 'problem reading url: ', url

global values
global file_json
wget('http://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&sensor=false')
