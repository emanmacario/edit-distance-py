# Program to calculate the local or global edit
# distance between two strings.
#
# Author: Emmanuel Macario
# Date: 26/03/19

import argparse
import numpy as np


def global_edit_distance(q, t):
    assert(q and t)

    lq = len(q)
    lt = len(t)

    # Initialise similarity matrix
    F = np.zeros((lq+1, lt+1), dtype=np.int64)
    for i in range(lq + 1):
        F[i, 0] = -i

    for j in range(lt + 1):
        F[0, j] = -j

    # print(F)

    # Compute similarity matrix
    for i in range(1, lq + 1):
        for j in range(1, lt + 1):
            match = 1 if q[i - 1] == t[j - 1] else -1
            F[i, j] = max(F[i - 1, j] - 1,          # Insertion
                          F[i, j - 1] - 1,          # Deletion
                          F[i - 1, j - 1] + match)  # Match/Mismatch

    # Print resultant matrix
    print(F)


def local_edit_distance(q, t):
    assert(q and t)
    pass


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', type=str, default='g',
                        help="local or global edit distance ('l'/'g')")
    args = parser.parse_args()
    return args


def main():
    args = set_options()

    # Input query and search strings
    q = input("Enter query string: ")
    t = input("Enter search string: ")

    # Calculate edit distance and print similarity matrix
    if args.type == 'l':
        local_edit_distance(q, t)
    elif args.type == 'g':
        global_edit_distance(q, t)
    else:
        print("Invalid type entered")
        exit()


if __name__ == "__main__":
    main()
