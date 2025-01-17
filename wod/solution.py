#!/usr/bin/env python3
"""Create Workout Of (the) Day (WOD)"""

import argparse
import csv
import os
import random
from tabulate import tabulate
from dire import die


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='wod.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num_exercises',
                        help='Number of exercises',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Make it easy',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    exercises = []

    for row in csv.DictReader(fh, delimiter=','):
        name = row['exercise']
        low, high = row['reps'].split('-')
        exercises.append((name, int(low), int(high)))

    return exercises


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    table = []

    for name, low, high in random.sample(exercises, k=args.num_exercises):
        if args.easy:
            low = int(low / 2)
            high = int(high / 2)

        table.append((name, random.randint(low, high)))

    print(tabulate(table, headers=('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()
