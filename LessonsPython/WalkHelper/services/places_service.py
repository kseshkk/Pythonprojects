from models.place import Place
from api.places_api import *

def get_places(city_name):
    parks = get_places_from_api(city_name, "park")
    cafes = get_places_from_api(city_name, "cafe")
    attractions = get_places_from_api(city_name, "attraction")

    result = []

    for i in range(2):
        result.append(parks[i])
        result.append(cafes[i])

        if len(result) < 5:
            result.append(attractions[i])

    return result