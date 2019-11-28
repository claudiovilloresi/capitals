#! /usr/bin/env python3

import argparse
from mypackages.capitals import check_capital, check_state



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('State', help='The name of the state')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    cp = check_capital(args.State)
    cs = check_state(args.State)
