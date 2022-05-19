import datetime

def extract_time_from_iso_format(time):
    timestamp = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z")
    formatted_time = datetime.datetime.strptime(f"{timestamp.hour}:{timestamp.minute}", "%H:%M")
    return formatted_time

def parse_time():
    return

  
def calculate_time_diff(time1, time2):
    return time1 - time2


def calculate_wake_time(arrival_time, prep_time, travel_time):
  return