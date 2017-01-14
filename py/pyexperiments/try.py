##import serial
###import time
##import appengineauth
##
##ser=serial.Serial("COM19",9600)
##watt=ser.readline()
##print watt
##sensornumber=1
##appengineauth.sendreport(sensornumber,watt)
##ser.close()
#
#
##import appengineauth
##appengineauth.sendreport(1,234.56)
#
import urllib
import urllib2
import serial
#app_url1='http://localhost:8084/post'+"?val="+str(255)
#
#app_url=urllib.urlencode(app_url1)
#
#req=urllib2.Request(app_url)
#resp=urllib2.urlopen(req)
#resp_body=resp.read()
#
#
#
##serv_uri = 'http://localhost:8084/post' + "?watt="+str(watt)
##
##serv_args = {}
##serv_args['continue'] = serv_uri
###serv_args['auth']     = authtoken
##    
##full_serv_uri =urllib.urlencode(serv_args)
##
##serv_req = urllib2.Request(full_serv_uri)
##serv_resp = urllib2.urlopen(serv_req)
##serv_resp_body = serv_resp.read()
#
##msg='hi'
ser=serial.Serial("COM20",9600)
msg1=ser.readline()
msg1=msg1.strip()
msg=ser.readline()
msg=msg.strip()
data={}
data['msg']=('%s'%msg)
data['sensorid']=('%s'%msg1)
url_values=urllib.urlencode(data)
print url_values
url='http://localhost:8082/report'
#url='http://sensdata.appspot.com/report'
full_url=url+'?'+url_values
data=urllib2.urlopen(full_url)
print data
req=urllib2.Request(url,url_values)
##print req
response=urllib2.urlopen(req)
the_page=response.read()




#msg='"hi",me'
#part=msg.split(',')
#new=part[0].strip('"')
#print new
