import argparse
from package_handler import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dimensions", help="the 3 dimensions of the package separated by whitespace in mm.", type=float, nargs='+')
    parser.add_argument("-w","--weight", help="the weight of the package in kg.", required = True,type=float)
    args = parser.parse_args()

    dimensions = args.dimensions
    weight = args.weight

    package = PackageHandler().get_package_type(dimensions, weight)
    
    if package:
        print(f"A {package['type']} package is required, costing ${package['cost']}.")
    else:
        print("The package cannot be shipped.")
