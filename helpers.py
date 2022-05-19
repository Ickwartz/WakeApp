import datetime

def extract_time_from_iso_format(time):
    '''
    Takes ISO 8601 datetime string and returns HH:MM datetime object
    '''
    timestamp = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z")
    formatted_time = datetime.datetime.strptime(f"{timestamp.hour}:{timestamp.minute}", "%H:%M")
    return formatted_time

def parse_time(time):
    '''
    Takes time string and returns it as HH:MM datetime object
    '''
    return datetime.datetime.strptime(time, "%H%M")

  
def calculate_time_diff(time1, time2):
    return time1 - time2


def calculate_wake_time(arrival_time, prep_time, travel_time):
    p_arrival_time = parse_time(arrival_time)
    p_prep_time = parse_time(prep_time)
    p_travel_time = parse_time(travel_time)
    return p_arrival_time - p_travel_time - p_prep_time