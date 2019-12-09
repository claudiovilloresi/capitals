#! /usr/bin/env python3

import argparse
from mypackages.capitals import check_capital, check_state


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, help='The name of the state')
    parser.add_argument('-c', type=str, help='The name of the capital')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    if args.s:
        cp = check_capital(args.s)
    else:
        cs = check_state(args.c)