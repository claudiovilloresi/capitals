#! /usr/bin/env python3

import argparse
import csv
import sqlite3
from mypackages.capitals import check_capital
from mypackages.capitals import check_state
from dbmanager import check_for_username_correct
from dbmanager import open_and_create
data = 'mypackages/list_of_capitals.csv'
db = 'sql.db'


def parse_allowed_input(datafile=data):
    """ Read data from csv file and create sets.
        Key arguments:
        - states: set of allowed states
        - capitals: set of allowed capitals
    """
    states = set()
    capitals = set()
    try:
        with open(datafile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            try:
                next(csv_reader)
            except StopIteration:
                return states, capitals
            for row in csv_reader:
                states.add(row[0])
                capitals.add(row[1])
    except FileNotFoundError:
        pass
    return states, capitals


def parse_arguments(states, capitals):
    """ Parse user inputs:
        -user: check username
        -p: check password
        -s: name of the states can be choosen from states set
        -c: name of the capitals can be choosen from capitals set
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-user',
        help="add a username (requires -p)",
        required=False)
    parser.add_argument(
        '-p',
        help="add a password (requires -p)",
        required=False)
    parser.add_argument(
        '-s',
        type=str,
        help='The name of the state',
        choices=states)
    parser.add_argument(
        '-c',
        type=str,
        help='The name of the capital',
        choices=capitals)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # Open the connection and if necessary create the users table
    open_and_create()
    states, capitals = parse_allowed_input()
    args = parse_arguments(states, capitals)
    # If the user is authenticate to proceed:
    if check_for_username_correct(args.user, args.p):
        # If user input is a state
        if args.s:
            cp = check_capital(args.s)
        # If user input is a capital
        else:
            cs = check_state(args.c)
    else:
        print("Username does not exist or password is incorrect")
