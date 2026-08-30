import requests

from models.place import Place

API_URL = "https://places-api.foursquare.com/places/search"
API_KEY = "Bearer GBXF4FPB3TJWH0GV3JAMBUIUJWSMTQGGP33W3BGPGL201Y4H"


def get_places_from_api(city_name, query):
    response = requests.get(
        API_URL,
        params={
        "query": query,
        "near": city_name,
        "limit": "5"
        },
        headers={
        "Authorization": API_KEY,
        "X-Places-Api-Version": "2025-06-17"
        },
        timeout=10
    )

    response.raise_for_status()
    data = response.json()

    places = []

    for current_place in data["results"]:
        places.append(Place(
            name=current_place["name"],
            latitude=current_place["latitude"],
            longitude=current_place["longitude"],
        ))

    return places