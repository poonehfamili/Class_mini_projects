from __future__ import print_function
import sys
import json
import csv
import numpy as np

MTA_KEY = 'a3a85cf2-ea31-4a06-bb9f-99676bb28d77'
BUS_LINE = 'B26'


#if not len(sys.argv) == 4:
   # print("Invalid number of arguments. Run as: python get_bus_info.py MTA_KEY BUS_LINE BUS_LINE.csv")
    # sys.exit()

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def get_jsonparsed_data(url):
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+ sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" +sys.argv[2] 
jsonData = get_jsonparsed_data(url)


fout = open(sys.argv[3], "w")
with open(sys.argv[3], 'wb') as f:
    writer = csv.writer(f)
    fout.write("Number of buses, Latitude, Longitude, Next Stop, Stop Status\n")
    number_of_B = len(jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    for i in range(number_of_B):
        bus = jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

        vehicle_location= bus[i]['MonitoredVehicleJourney']['VehicleLocation']
    #print("BUS NUMBER %i is at %f latitude and %f longtitude" % (i, vehicle_location['Latitude'], vehicle_location['Longitude']))

        if 'OnwardCall' not in bus[i]["MonitoredVehicleJourney"]['OnwardCalls']:
            next_stop = "N/A"
            stop_status = "N/A"
        else:
            next_stop = bus[i]["MonitoredVehicleJourney"]['OnwardCalls']['OnwardCall'][0]["StopPointName"]

    #print("Next Stop is %s" % ( next_stop ))

            stop_status = bus[i]["MonitoredVehicleJourney"]['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    # print("Stop_Status is %s" % ( stop_status ))
        fout.write("%s,%s,%s,%s\n" %(vehicle_location['Latitude'], vehicle_location['Longitude'], next_stop, stop_status))



fout.close()