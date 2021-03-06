from __future__ import print_function
import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
#from __future__ import print_function
import sys

APIkey = sys.argv[1]
Busnumber = sys.argv[2]

# &VehicleMonitoringDetailLevel=calls&LineRef=B52

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="%(APIkey, Busnumber)

#%pylab inline
pl.rc('font', size=15)


#url = "http://api.openweathermap.org/data/2.5/weather?q=NewYork&mode=Json&units=metric&&cnt=7&APPID=XXXXXXXXXXXXXXXXXXXXXXXX"
#url = "http://api.openweathermap.org/data/2.5/weather?q=" + \"New York&APPID=" + os.getenv("OPENWEATHERKEY") 

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + APIkey +"&VehicleMonitoringDetailLevel=calls&LineRef=" + Busnumber

#url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=5dc94621-9d04-4fcd-9ba3-ad0becad6af7&VehicleMonitoringDetailLevel=calls&LineRef=B52"    

#busnumber= 
#os.environ["BUSAPIKEY"] = "5dc94621-9d04-4fcd-9ba3-ad0becad6af7"
#apikey = os.getenv("BUSAPIKEY")



print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
print(data)


Howmanybuses = len(data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"])
print(Howmanybuses)

print('Bus Line',Busnumber)
print('Number of Active Buses : ', Howmanybuses)



fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

for i in range(Howmanybuses):
    try:
        contents = data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'],\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        strcontents = str(contents) +'\n'
        fout.write(strcontents)    
    except:
        contents = data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],\
      
        strcontents = str(contents) + ",N/A," + "N/A" +'\n'
        fout.write(strcontents)    



'''
    data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],',',\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],\',',\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'],\',',\
          data['Siri']['ServiceDelivery']["VehicleMonitoringDelivery"][0]["VehicleActivity"][i]\
['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']\n
'''



    