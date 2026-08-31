import requests
from models.city import City

GEONAMES_SEARCH_URL = "https://secure.geonames.org/searchJSON"
USERNAME = "ks3shkkk" 


def is_city_exist(city_name):
    response = requests.get(
        GEONAMES_SEARCH_URL,
        params={
            "q": city_name,
            "maxRows": 1, 
            "featureClass": "P", 
            "lang": "ru",
            "username": USERNAME,
            "countryCode": "RU", 
        },
        timeout=10,
    )

    response.raise_for_status()

    cities_data = response.json()["geonames"]
    if len(cities_data) == 0:
        return False

    return True


