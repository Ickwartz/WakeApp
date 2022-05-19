from sqlite3 import Timestamp
from urllib import response
import requests
import json
import helpers


# NOTE: BVG API has /stops/nearby to query for stops near a geolocation

def get_stop_id(stop):
    '''
    Takes a stop and returns id from BVG Api
    '''
    url = 'https://v5.bvg.transport.rest/locations'
    parameters = {
        "poi": "false",
        "addresses": "false",
        "query": stop
    }

    response = requests.get(url, params=parameters)
    response_json = json.loads(response.text)
    return response_json[0]["id"]


def get_travel_time(stop_1, stop_2, arrival):
    stop_id_1 = get_stop_id(stop_1)
    stop_id_2 = get_stop_id(stop_2)

    url = 'https://v5.bvg.transport.rest/journeys'
    parameters = {
        "from": stop_id_1,
        "to": stop_id_2,
        "arrival": arrival
    }

    response = requests.get(url, params=parameters)
    response_json = json.loads(response.text)

    journey = response_json["journeys"][0]["legs"]

    departure_time = helpers.extract_time_from_iso_format(journey[0]["departure"])
    time_of_arrival = helpers.extract_time_from_iso_format(journey[-1]["arrival"])

    return helpers.calculate_time_diff(time_of_arrival, departure_time)