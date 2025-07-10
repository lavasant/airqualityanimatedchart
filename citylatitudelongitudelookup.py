import json
with open('json/airquality-covid19-cities.json', 'r') as file:

    json = json.load(file)

def lookupcitylatitudeandlongitude(city):
    for i in json["data"]:
        if city == i["Place"]["name"]:
            latitudelongitude = i["Place"]["geo"]
    return latitudelongitude
