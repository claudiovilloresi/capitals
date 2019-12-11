#! /usr/bin/env python3

import argparse
import csv
from mypackages.capitals import check_capital, check_state
data ='mypackages/list_of_capitals.csv'

def parse_allowed_input(datafile=data):
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, help='The name of the state', choices=states)
    parser.add_argument('-c', type=str, help='The name of the capital', choices=capitals)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
  states, capitals = parse_allowed_input()
  args = parse_arguments(states, capitals)
  if args.s:
      cp = check_capital(args.s)
  else:
      cs = check_state(args.c)
