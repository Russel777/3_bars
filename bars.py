import json

from math import sqrt

import sys


def load_data(filepath):
    with open(filepath) as file:
        return json.loads(file.read())


def get_biggest_bar(data):
    max = 0
    bar_name = ''
    for bar in data["features"]:
        seatsCount = bar["properties"]["Attributes"]["SeatsCount"]
        if seatsCount > max:
            max = seatsCount
            bar_name = bar["properties"]["Attributes"]["Name"]
    return bar_name


def get_smallest_bar(data):
    min = 1000000000
    bar_name = ''
    for bar in data["features"]:
        seatsCount = bar["properties"]["Attributes"]["SeatsCount"]
        if seatsCount < min:
            min = seatsCount
            bar_name = bar["properties"]["Attributes"]["Name"]
    return bar_name


def get_closest_bar(data, longitude, latitude):
    path = 1000000000
    bar_name = ''
    for bar in data["features"]:
        bar_coordinates = bar["geometry"]["coordinates"]
        new_path = sqrt((bar_coordinates[0]-longitude)**2 + (bar_coordinates[1]-latitude)**2)
        if new_path < path:
            path = new_path
            bar_name = bar["properties"]["Attributes"]["Name"]
    return bar_name


if __name__ == '__main__':
    data = load_data('bars.json')
    print('Biggest bar is {}'.format(get_biggest_bar(data)))
    print('Smallest bar is {}'.format(get_smallest_bar(data)))
    if len(sys.argv) > 1:
        print('Closest bar is {}'.format(get_closest_bar(data, float(sys.argv[1]), float(sys.argv[2]))))
