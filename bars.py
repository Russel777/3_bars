import json
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="path to the file")
    parser.add_argument("--biggest", help="display a biggest bar in file list", action="store_true")
    parser.add_argument("--smallest", help="display a smallest bar in file list", action="store_true")
    parser.add_argument("-x",
                        "--longtitude",
                        help="input longitude and latitude for display a closest bar in file list ",
                        type=float)
    parser.add_argument("-y",
                        "--latitude",
                        help="input longitude and latitude for display a closest bar in file list ",
                        type=float)
    args = parser.parse_args()
    if args.path:
        json_content = load_data(args.path)
        if args.biggest:
            print('Biggest bar is {}'.format(get_biggest_bar(json_content)))
        if args.smallest:
            print('Smallest bar is {}'.format(get_smallest_bar(json_content)))
        if args.longtitude and args.latitude:
            print('Closest bar is {}'.format(get_closest_bar(json_content, args.longtitude, args.latitude)))
        elif args.longtitude or args.latitude:
            print('Not enough parameters')
    else:
        print("Enter path")
