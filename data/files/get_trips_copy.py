import os
import json
import calendar
import logging

#!pip install sodapy
from sodapy import Socrata

def get_trips_data(month):
    """
    Requests trips data from the city of Chicago for a single month in 2021
    """

    url = "data.cityofchicago.org"
    client = Socrata(url, None, timeout=60)

    # Dataset: Transport Network Provider City of Chicago 2021
    # https://data.cityofchicago.org/Transportation/Transportation-Network-Providers-Trips-2021/unf9-2zu4
    identifier = "unf9-2zu4"
    
    end_of_month = calendar.monthrange(2021, month)
    #total_trips = {}

    for i in range(1, end_of_month[1] + 1):
        logging.info(f"Retrieving trips data, month {month}, day {i}")
        trips = client.get(identifier, where=f"trip_start_timestamp >= '2021-{month}-{i}T00:00:00.000' AND trip_start_timestamp <= '2021-{month}-{i}T23:59:59.999'", limit=500000, order="trip_start_timestamp")
        
        logging.info(f"Writing file, month {month}, day {i}")
        filename = f"data/trips_data/{month}/trips_2021_{month}_{i}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            json.dump(trips, f)

        logging.info(f"Trips recorded, month {month}, day {i}: {len(trips)}")
        print(f"Trips recorded, month {month}, day {i}: {len(trips)}")

        #total_trips[f"{month}-{i}"] = len(trips)
        #print(sum(total_trips.values()))

def main():
    for i in range(1, 13):
        get_trips_data(i)

if __name__ == "__main__":
    main()