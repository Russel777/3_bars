import argparse
import json

from math import sqrt


def load_data(filepath):
    with open(filepath) as file:
        return json.loads(file.read())


def get_biggest_bar(bars):
    return max(
        bars,
        key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"],
    )


def get_smallest_bar(bars):
    return min(
        bars,
        key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"],
    )


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bar: sqrt(
            (bar["geometry"]["coordinates"][0] - longitude)**2 +
            (bar["geometry"]["coordinates"][1] - latitude)**2
        )
    )


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        help="path to the file",
        required=True,
    )
    parser.add_argument(
        "--biggest",
        help="display a biggest bar in file list",
        action="store_true",
    )
    parser.add_argument(
        "--smallest",
        help="display a smallest bar in file list",
        action="store_true",
    )
    parser.add_argument(
        "-x",
        "--longtitude",
        help="input longitude and latitude for display a "
             "closest bar in file list ",
        type=float,
    )
    parser.add_argument(
        "-y",
        "--latitude",
        help="input longitude and latitude for display a "
             "closest bar in file list ",
        type=float,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_argv()
    bars = load_data(args.path)["features"]
    if args.biggest:
        print("Biggest bar is {}".format(
            get_biggest_bar(bars)["properties"]["Attributes"]["Name"])
        )
    if args.smallest:
        print("Smallest bar is {}".format(
            get_smallest_bar(bars)["properties"]["Attributes"]["Name"])
        )
    if args.longtitude and args.latitude:
        print("Closest bar is {}".format(
            get_closest_bar(
                bars,
                args.longtitude,
                args.latitude
            )["properties"]["Attributes"]["Name"],
            )
        )
    elif args.longtitude or args.latitude:
        print("Not enough parameters")
