# developed by Shivam Jumani. I took help from Youtube videos to understand how to analyse a JSON file. I also referred to someone's GITHUB repo to find code that carried out a similar function to use the loop function to search for 'n' in the JSON file. It took me a while to understand the syntax, and at times I had to ask small questions to a friend outside of CUSP who is familiar with python.

from __future__ import print_function
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

import csv

if not len(sys.argv) == 4:
    print("Invalied number of arguments. USAGE: python show_bus_locations.py <MTA KEY> <BUS_LINE> <BUS_LINE.csv>")
    sys.exit()

key = sys.argv[1]
bus_line = sys.argv[2]

bus_url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key='+key+'&VehicleMonitoringDetailLevel=calls&LineRef='+bus_line

response = urllib.urlopen(bus_url)
busdata = response.read().decode("utf-8")
busdata = json.loads(busdata)

fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

if not busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0].get('VehicleActivity'):
    print('Number of Active Buses : 0')
else:
    no_of_buses = len(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    
for n in (range(0, no_of_buses)):

    bus_lat = busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    bus_lon = busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    try: 
      bus_stop = busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    except LookupError:
      bus_stop = "N/A"
     
    try:
      bus_status = busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    except LookupError:
      bus_status = "N/A"

    fout.write("%s,%s,%s,%s\n" %(bus_lat, bus_lon, bus_stop, bus_status))

fout.close()
