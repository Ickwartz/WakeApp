from sqlite3 import Timestamp
from urllib import response
import requests
import json
import datetime


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


def get_travel_time(stop_id_1, stop_id_2, arrival):
    url = 'https://v5.bvg.transport.rest/journeys'
    parameters = {
        "from": stop_id_1,
        "to": stop_id_2,
        "arrival": arrival
    }

    response = requests.get(url, params=parameters)
    response_json = json.loads(response.text)
    journey = response_json["journeys"][0]["legs"]
    departure_time = extract_time_from_iso_format(journey[0]["departure"])
    time_of_arrival = extract_time_from_iso_format(journey[-1]["arrival"])
    return time_of_arrival - departure_time


def extract_time_from_iso_format(time):
    timestamp = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z")
    formatted_time = datetime.datetime.strptime(f"{timestamp.hour}:{timestamp.minute}", "%H:%M")
    return formatted_time


start_id = get_stop_id("vincent-van-gogh-str")
stop_id = get_stop_id("neukoelln")

print(get_travel_time(start_id, stop_id, "12:00"))
