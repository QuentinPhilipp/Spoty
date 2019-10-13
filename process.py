import json

file_object = open("worldSpots.txt","r")

line = file_object.readline()


class Spot(object):
    """docstring for Spot."""

    def __init__(self, lat,lon,name):
        self.lat = lat,
        self.lon = lon,
        self.name = name
        self.ranking = ranking

n=0
subStrings = []
start = 0
end = 0

for index in range(len(line)):
    if(line[index]=='{'):
        start=index
    elif(line[index]=='}'):
        end=index
        subStrings.append(line[start:end])

spotList = []

for spot in subStrings:
    latIndex = spot.find("lat")
    lonIndex = spot.find("lon")
    nameIndex = spot.find("name")
    end = spot.find("spotRank")

    lat = spot[latIndex+5:latIndex+15]
    lon = spot[lonIndex+5:lonIndex+15]
    name = spot[nameIndex+7:end-3]
    ranking = spot[end+10:]

    # print(lat)
    # print(lon)
    # print(name)
    # print(ranking)
    try:
        floatLat = float(lat)
        floatLon = float(lon)
        spot = Spot(floatLat,floatLon,name)
        spotList.append(spot)
    except Exception as e:
        pass






with open('newSpot.geojson', 'w', encoding='utf-8') as f:
    for elem in spotList:
        print(elem.lat)
        print(elem.lon)
        print(elem.name)
        print("\n")
        data = {
        "type": "Feature",
        "geometry": {
           "type": "Point",
           "coordinates": [elem.lon[0],elem.lat[0]]
        },
        "properties": {
        "name": elem.name,
        "ranking":elem.ranking
        }
        }
        json.dump(data,f,ensure_ascii=False, indent=4)

print(len(spotList))




# with open('worldSpots.txt') as f:
#     json_data = json.load(f)
#     print(json_data)
