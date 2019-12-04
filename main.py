#! /usr/bin/env python3

import argparse
from mypackages.capitals import check_capital
valid_states = ['list_of_capitals']


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('State', help='The name of the state',choices=valid_states)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    cp = check_capital(args.State)
    #print ('The capital of "{}" is "{}"' .format(args.State, cp))
