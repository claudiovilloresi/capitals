#! /usr/bin/env python3

import argparse
import csv
import sqlite3
from mypackages.capitals import check_capital, check_state
from sql_test import check_for_username_correct, open_and_create, parse_args
data ='mypackages/list_of_capitals.csv'
db = 'sql.db'

def parse_allowed_input(datafile=data):
  states = set()
  capitals = set()
  with open(datafile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
            states.add(row[0])
            capitals.add(row[1])
  return states, capitals

def parse_arguments(states, capitals):
    parser = argparse.ArgumentParser()
    parser.add_argument('-user', help="add a username (requires -p)", required=False)
    parser.add_argument('-p', help="add a password (requires -p)", required=False)
    parser.add_argument('-s', type=str, help='The name of the state', choices=states)
    parser.add_argument('-c', type=str, help='The name of the capital', choices=capitals)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    open_and_create()

    states, capitals = parse_allowed_input()
    args = parse_arguments(states, capitals)
    if check_for_username_correct(args.user, args.p):
        if args.s:
              cp = check_capital(args.s)
        else:
              cs = check_state(args.c)
    else:
         print ("Username does not exist or password is incorrect")
