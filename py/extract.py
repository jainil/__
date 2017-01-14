
#from string import Template


#infile='Devore.txt'
infile='quake.txt'
f=open(infile)
outfile='pickies.txt'
w=open(outfile,'w')

#extracting region of interest
##for line in f:
##  columns=line.split(' ')#2012 04 28 15:05:00.566 UTC 25681043 0.0 0.0 0.002572834462285411 34.175739,-118.112030 2012 04 28 15:05:00.998 UTC
##  column2=columns[4].split('\t')
##  timesplit=columns[3].split(':')
##  identity=column2[1]
##  if timesplit[0]=='15':
##    if int(timesplit[1]) in range(5,10):


#extracting sensorlist
##sensorid=[]
##i=0
##
##for line in f:
##  columns=line.split(' ')
##  column2=columns[4].split('\t')
##  #print columns, column2
##  #break
##  identity=column2[1]
##  if identity not in sensorid:
##    sensorid.append(identity)
##    coord=column2[5].split(',')
##    w.write("station['"+identity+"']={center: new google.maps.LatLng("+coord[0]+","+coord[1]+")};\n")
##    i=i+1
##    
##print i

##prevsec=-1
##picks=[]
##slist=[]
##for i in range(0,300):
##  picks[i]=[]

picks={}

#time list(going by the second now: datetime is messed up)
for line in f:
  columns=line.split(' ')#2012 04 28 15:05:00.566 UTC 25681043 0.0 0.0 0.002572834462285411 34.175739,-118.112030 2012 04 28 15:05:00.998 UTC
  column2=columns[4].split('\t')
  timesplit=columns[3].split(':')
  sec=int(round(float(timesplit[2]))+(60*(int(timesplit[1])-5)))
##  if sec!=prevsec:
##    print sec
##    picks.append(slist)
##    prevsec=sec#prevsec+1
##    slist=[]
  identity=column2[1]
##  slist.append(identity)
  if sec in picks.keys():
    picks[sec].append(identity)
  else:
    picks[sec]=[identity]
  
#since we dont have all seconds, we have to create empty instances of picks[THATsecond]
for i in range(1,300):
  if i not in picks.keys():
    picks[i]=[]

#write for javascript
for sec in picks.keys():
  ids='(%s)' % ', '.join(map(str, picks[sec]))
  w.write("time['"+str(sec) +"']={stations: new Array"+ ids +"};\n")

f.close()
w.close()
