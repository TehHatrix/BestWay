import json
import gmplot
from geopy.geocoders import Nominatim
import googlemaps
from geopy import distance

thegmap = googlemaps.Client(key ='AIzaSyDKD-hoJriZ9KxFdkhPTw0c9PBhCEEKt4I')
geolocator = Nominatim(user_agent="geoAPIExercise")
location5 = geolocator.geocode("Petronas Twin Towers")
gmapone = gmplot.GoogleMapPlotter(location5.latitude,location5.longitude,13)
pwtc = geolocator.geocode("World Trade Centre, Kuala Lumpur")
klcc = geolocator.geocode("Suria KLCC")
zouk = geolocator.geocode("Zouk Club Kuala Lumpur")
dataran = geolocator.geocode("Dataran Merdeka")
thelatofnodes = []
thelongofnodes = []
#thelatofnodes.append(pwtc.latitude)
thelatofnodes.append(klcc.latitude)
thelatofnodes.append(zouk.latitude)
thelatofnodes.append(dataran.latitude)
#thelongofnodes.append(pwtc.longitude)
thelongofnodes.append(klcc.longitude)
thelongofnodes.append(zouk.longitude)
thelongofnodes.append(dataran.longitude)


def extractjson(thejson):
    lat = []
    long = []
    coor = []
    dalengthcoordinates = 0
    with open(thejson, 'r') as f:
        data = json.load(f)
    length = len(data['features'][0]['geometry']["coordinates"])
    while dalengthcoordinates < length:
        dalat = data['features'][0]['geometry']["coordinates"][dalengthcoordinates][1]
        dalong = data['features'][0]['geometry']["coordinates"][dalengthcoordinates][0]
        long.append(dalong)
        lat.append(dalat)
        coor.append([dalat, dalong])
        dalengthcoordinates = dalengthcoordinates + 1
    i = 0
    total = 0;
    while i < len(coor) - 1:
        total += distance.distance(coor[i], coor[i + 1]).km
        i = i + 1
    return coor

def getsnappedlat(thejsoncoor):
    snappedlat = []
    thelist = thegmap.snap_to_roads(thejsoncoor)
    with open('thedata.json', 'w') as outfile:
        json.dump(thelist, outfile, indent=4)
    with open('thedata.json', 'r') as f:
        data = json.load(f)
    for thedata in data:
        snappedlat.append(thedata['location']['latitude'])
    return snappedlat

def getsnappedlong(thejsoncoor):
    snappedlong = []
    thelist = thegmap.snap_to_roads(thejsoncoor)
    with open('thedata.json', 'w') as outfile:
        json.dump(thelist, outfile, indent=4)
    with open('thedata.json', 'r') as f:
        data = json.load(f)
    for thedata in data:
        snappedlong.append(thedata['location']['longitude'])
    return snappedlong


gmapone.scatter(thelatofnodes,thelongofnodes,'purple',size = 50, marker = False)
gmapone.plot(getsnappedlat(extractjson('klcctopwtc.json')),getsnappedlong(extractjson('klcctopwtc.json')),'green',edge_width = 5)
gmapone.plot(getsnappedlat(extractjson('klcctodataran.json')),getsnappedlong(extractjson('klcctodataran.json')),'purple',edge_width = 5)
gmapone.plot(getsnappedlat(extractjson('klcctozouk.json')),getsnappedlong(extractjson('klcctozouk.json')),'blue',edge_width = 5)
gmapone.draw("realtest2.html")
