import argparse
import json

from math import sqrt


def load_data(filepath):
    with open(filepath) as file:
        return json.loads(file.read())


def get_biggest_bar(bars):
    return max(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bars):
    return min(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(bars, longitude, latitude):
    path = 1000000000
    bar_name = ''
    for bar in bars:
        bar_coordinates = bar["geometry"]["coordinates"]
        new_path = sqrt((bar_coordinates[0] - longitude)**2 + (bar_coordinates[1] - latitude)**2)
        if new_path < path:
            path = new_path
            bar_name = bar["properties"]["Attributes"]["Name"]
    return bar_name


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="path to the file", required=True)
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

    json_content = load_data(args.path)["features"]
    if args.biggest:
        print('Biggest bar is {}'.format(
            get_biggest_bar(json_content)["properties"]["Attributes"]["Name"])
        )
    if args.smallest:
        print('Smallest bar is {}'.format(
            get_smallest_bar(json_content)["properties"]["Attributes"]["Name"])
        )
    if args.longtitude and args.latitude:
        print('Closest bar is {}'.format(get_closest_bar(json_content, args.longtitude, args.latitude)))
    elif args.longtitude or args.latitude:
        print('Not enough parameters')


if __name__ == '__main__':
    arguments()
