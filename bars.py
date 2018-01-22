import json

from math import sqrt

import sys


def load_data(filepath):
    with open(filepath) as file:
        return json.loads(file.read())


def get_biggest_bar(json_content):
    bars_dict = {}
    for bar in json_content["features"]:
        bars_dict[bar["properties"]["Attributes"]["SeatsCount"]] = bar["properties"]["Attributes"]["Name"]
    return bars_dict[max(bars_dict.keys())]


def get_smallest_bar(json_content):
    bars_dict = {}
    for bar in json_content["features"]:
        bars_dict[bar["properties"]["Attributes"]["SeatsCount"]] = bar["properties"]["Attributes"]["Name"]
    return bars_dict[min(bars_dict.keys())]


def get_closest_bar(json_content, longitude, latitude):
    path = 1000000000
    bar_name = ''
    for bar in json_content["features"]:
        bar_coordinates = bar["geometry"]["coordinates"]
        new_path = sqrt((bar_coordinates[0] - longitude)**2 + (bar_coordinates[1] - latitude)**2)
        if new_path < path:
            path = new_path
            bar_name = bar["properties"]["Attributes"]["Name"]
    return bar_name


if __name__ == '__main__':
    json_content = load_data('bars.json')
    print('Biggest bar is {}'.format(get_biggest_bar(json_content)))
    print('Smallest bar is {}'.format(get_smallest_bar(json_content)))
    if len(sys.argv) > 1:
        print('Closest bar is {}'.format(get_closest_bar(json_content, float(sys.argv[1]), float(sys.argv[2]))))
