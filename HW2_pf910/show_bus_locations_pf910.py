import sys
import json

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]



try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

def show_bus_locations(MTA_KEY, BUS_LINE):
    def get_jsonparsed_data(url):
        response = urllib.urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    url ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ MTA_KEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" +BUS_LINE 
    jsonData = get_jsonparsed_data(url)

    number_of_B = len(jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    bus = jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    for i in range(number_of_B):
        vehicle_location= bus[i]['MonitoredVehicleJourney']['VehicleLocation']
        print("BUS NUMBER %i is at %f latitude and %f longtitude" % (i, vehicle_location['Latitude'], vehicle_location['Longitude']))

show_bus_locations(MTA_KEY, BUS_LINE)