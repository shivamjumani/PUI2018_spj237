from __future__ import print_function
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print("Invalied number of arguments. USAGE: python show_bus_locations.py <MTA KEY> <BUS_LINE>")
    sys.exit()

key = sys.argv[1]
bus_line = sys.argv[2]

bus_url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key='+key+'&VehicleMonitoringDetailLevel=calls&LineRef='+bus_line

response = urllib.urlopen(bus_url)
busdata = response.read().decode("utf-8")
busdata = json.loads(busdata)

print("Bus Line : " + bus_line)
if not busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0].get('VehicleActivity'):
    print('Number of Active Buses : 0')
else:
    print("Number of Active Buses : " + str(len(busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])))
    
i=0
for routes in busdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]:
    if routes.get('VehicleActivity'):
        for bus in routes["VehicleActivity"]:
            print("Bus " +str(i)+ " is at latitude " + str(bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]) + " and longitude " + str(bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]))
            i+=1
    